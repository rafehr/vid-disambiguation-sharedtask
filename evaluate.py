#!/usr/bin/env python
import sys
import os
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('train', help='Path to training set.')
arg_parser.add_argument('gold', help='Path to dev set with gold annotations.')
arg_parser.add_argument('preds', help='Path to dev set with predictions.')

VALID_LABELS = ['figuratively', 'literally', 'undecidable', 'both']

def compute_scores(gold, preds):
    """Computes the precision, recall and F1 score for the predictions.

    Parameters:
            gold (list): The gold labels.
            preds (list): The predicted labels.

    Returns:
            precision (float): The precision score.
            recall (float): The recall score.
            f1 (float): The F1 score.
    """
    tp = float(sum([1 for t, p in zip(gold, preds) if t == u'literally' and p == u'literally']))
    fn = float(sum([1 for t, p in zip(gold, preds) if t == u'literally' and p != u'literally']))
    fp = float(sum([1 for t, p in zip(gold, preds) if t != u'literally' and p == u'literally']))
    
    precision = (tp/(tp + fp)) if tp != 0 else 0
    recall = (tp/(tp + fn)) if tp != 0 else 0
    f1 = (2*precision*recall)/(precision + recall) if tp != 0 else 0

    return precision, recall, f1

def get_labels(train_path, gold_path, pred_path):
    """Reads the train, gold and prediction data and returns the gold and
    predicted labels as well as the indices of the unseen VID type instances.

    Parameters:
        train_path (str): Path to train data.
        gold_path (str): Path to gold data.
        pred_path (str): Path to data with predictions.

    Returns:
        gold_labels (list): List with gold labels.
        pred_labels (list): List with predicted labels.
        unseen_types_idxs (list): List with indices of the unseen VID type instances.
    """
    with open(train_path, 'r', encoding='utf-8') as t:
        train_data = [i.split('\t') for i in t.read().rstrip().split('\n')]
    train_vid_types = set([i[1] for i in train_data])

    with open(gold_path, 'r', encoding='utf-8') as g:
        gold_data = [i.split('\t') for i in g.read().rstrip().split('\n')]
    gold_vid_types = set([i[1] for i in gold_data])
    gold_labels = [i[2] for i in gold_data]
    unseen = list(gold_vid_types - train_vid_types)
    unseen_idxs = [idx for idx, i in enumerate(gold_data) if i[1] in unseen]

    with open(pred_path, 'r', encoding='utf-8') as p:
        pred_data = [i.split('\t') for i in p.read().rstrip().split('\n')]
    pred_labels = [i[2] for i in pred_data]

    # Sanity check for prediction data
    for row in pred_data:
            assert len(row) == 4, "The number of elements in a row does not equal four."
    assert len(pred_data) == len(gold_data), "Gold and prediction data are not of equal length."
    for p in set(pred_labels):
        assert p in VALID_LABELS, "Predicted label is not one of the valid labels."

    return gold_labels, pred_labels, unseen_idxs

if __name__ == '__main__':
    args = arg_parser.parse_args()
    train_path = args.train
    gold_path = args.gold
    pred_path = args.preds

    gold_labels, pred_labels, unseen_idxs = get_labels(train_path, gold_path, pred_path)
    
    assert len(pred_labels) == len(gold_labels)

    precision, recall, f1 = compute_scores(gold_labels, pred_labels)

    print("F1-all: {}".format(f1))

    gold_labels_unseen = list(map(gold_labels.__getitem__, unseen_idxs))
    pred_labels_unseen = list(map(pred_labels.__getitem__, unseen_idxs))

    precision, recall, f1 = compute_scores(gold_labels_unseen, pred_labels_unseen)

    print("F1-unseen: {}".format(f1))




