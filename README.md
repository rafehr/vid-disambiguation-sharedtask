**Update (08.11.2021)**: The proceedings of the shared task workshop are now online: https://konvens.org/proceedings/2021/.

**Update (23.08.2021)**: The program for the shared task workshop now can be found below.

**Update (14.07.21)**: Labeled test data (test.tsv) now available!

**Update (22.06.21)**: Test data (test_blind.tsv) now available!

**Update (19.05.21)**: There have been some duplicate ids in the dataset. Those have been removed.

**Update (15.05.21)**: Training data (train.tsv, dev.tsv and dev_blind.tsv) now available!

**Official CodaLab site**: https://competitions.codalab.org/competitions/31715

## Shared task workshop program (September 6th, 14:00–17:00):

|Timeslot|Talk|
|:--------|:----|
|14:00 - 14:20| [Introduction (Rafael Ehren, Laura Kallmeyer, Timm Lichte, Jakub Waszczuk)](https://konvens.org/proceedings/2021/papers/KONVENS_2021_Disambiguation_ST-Shared_Task_on_the_Disambiguation_of_German_Verbal_Idioms_at_KONVENS_2021.pdf)|
|14:20 - 14:50| [Shallow Context Analysis for German Idiom Detection (Miriam Amin, Peter Fankhauser, Marc Kupietz, Roman Schneider)](https://konvens.org/proceedings/2021/papers/KONVENS_2021_Disambiguation_ST-Shallow_Context_Analysis_for_German_Idiom_Detection.pdf)
|14:50 - 15:00| Break
|15:00 - 15:30| [Cracking a Walnut with a Sledgehammer: XLM-RoBERTa for German Verbal Idiom Disambiguation Tasks (Franziska Pannach, Tillmann Dönicke)](https://konvens.org/proceedings/2021/papers/KONVENS_2021_Disambiguation_ST-XLM-RoBERTa_for_German_Verbal_Idiom_Disambiguation_Tasks.pdf)
|15:30 - 16:00| [Verbal Idioms: Concrete Nouns in Abstract Contexts (Jean Charbonnier, Christian Wartena)](https://konvens.org/proceedings/2021/papers/KONVENS_2021_Disambiguation_ST-Verbal_Idioms_Concrete_Nouns_in_Abstract_Contexts.pdf)
|16:00 - 16:10| Break
|16:10 - 17:00| Informal discussion

# Shared Task on the Disambiguation of German Verbal Idioms

This is the official repository for the shared task on the disambiguation of German verbal idioms which is organized in connection with [KONVENS 2021](https://konvens2021.phil.hhu.de/). Here you will find all the data necessary to participate in the shared task.

## The task

The identification of verbal multiword expressions (VMWEs) is a well known challenge in the natural language processing (NLP) community and has received a lot of attention in recent years - especially thanks to the [PARSEME](https://typo.uni-konstanz.de/parseme/index.php/organization) network (PARsing and Multiword Expressions) which organized three shared tasks on this topic in [2017](https://www.diva-portal.org/smash/get/diva2:1167953/FULLTEXT01.pdf), [2018](https://hal.archives-ouvertes.fr/hal-01865575/file/2018-Ramisch-et-al.pdf) and [2020](https://www.aclweb.org/anthology/2020.mwe-1.14.pdf). But while the PARSEME shared tasks were highly multilingual and targeted all VMWE types, we will focus only on German verbal idioms (VIDs). Furthermore, we concentrate on a subtask of the identification process which is the disambiguation of VIDs and their literal counterparts. E.g. if we consider the utterance "Kim is talking to Huey on the big white telephone" we have the two distinct possibilities that Kim is either sick or that she is actually talking to a person called Huey on the phone. The task is to automatically decide for cases like this if the expression has its literal or its idiomatic meaning.

## The data

The shared task data consists of 9906 instances of a German VID type or its literal counterpart in context. The set of VID types was pre-selected, thus it constitutes a lexical sample data set. It is a merger of the [COLF-VID](https://www.aclweb.org/anthology/2020.figlang-1.29.pdf) and the [German SemEval-2013 task 5b](https://www.aclweb.org/anthology/S13-2007.pdf) data sets. Consider this example:

```
T890202.28.4077	in wasser fallen	figuratively	Der Streit ums Hormonfleisch zwischen USA und EG provozierte den Polizeieinsatz . Aber nicht nur der Steakverkauf , auch die Aktionen gegen den Hormonstand , auf die sich Gruppen der Bauernopposition schon vorbereitet hatten , <b>fielen</b> <b>ins</b> <b>Wasser</b> . Die Fleischexporteure der USA wollten ihrerseits die " Grüne Woche " zur " Aufklärung " nutzen .
```

The data comes in tsv files and every line has the following format:

> Instance id \t VID type \t label \t text

So the first column contains the id (```T890202.28.4077``` in the example), the second the VID type (```in wasser fallen```), the third the label (```figuratively```) and the fourth the sentence with either the instance of the VID type or its literal counterpart (and two additional context sentences). The parts of the target expression are marked with the ```<b>``` tag (```<b>fielen</b> <b>ins</b> <b>Wasser</b>```). This means, we assume that another process has already pre-identified the target expressions and the systems only need to decide on the correct reading. There will be four possible labels: ```figuratively```, ```literally```, ```undecidable``` and ```both```. The first two should be self-explanatory. The label ```undecidable``` was used by the annotators if it was not possible to disambiguate an instance given the context. The label ```both``` was applied when both the literal and the idiomatic readings were active. But since in more than 99% of the cases it was either either literal or idiomatic, at the end it basically can be treated as a binary task.

## The timeline

- ~~Trial data ready: April 23, 2021~~
- ~~Training data ready: May 15, 2021~~
- ~~Test data ready: June 23, 2021~~
- ~~Evaluation end: June 30, 2021~~
- ~~Paper submission due: July 15, 2021~~
- ~~Camera ready due: August 10, 2021~~
- ~~Konvens converence: September 6–10, 2021~~

## The evaluation

The participating teams will be required to submit the test data with the predictions made by their systems. This will be the format of the test data:

```T861224.44.1377	auf tisch liegen	NONE	Band drei vom " Kapital " , die Nummer 25 der blauen Marx-Engels-Werke aus dem Ost-Berliner Dietz-Verlag , wird aufgeschlagen . Ganz weit hinten , so daß das Buch im kräftigem Pappeinband nicht richtig <b>auf</b> dem <b>Tisch</b> <b>liegen</b> will . " Die Klassen " heißt das letzte Kapitel .```

It is the same as the training data with the only difference being that in place of the label one can find the placeholder ```NONE```. These placeholders are to be replaced by the labels the systems predict.

We will use [CodaLab](https://codalab.org/) for evaluation. This is the official CodaLab site where you will find all the information you need to participate: https://competitions.codalab.org/competitions/31715

In addition, we provide the evaluation script ```evaluate.py``` that can be used by the participants to evaluate their systems outside of CodaLab. It takes as input the train set (```train.tsv```), the dev set with the gold labels (```dev.tsv```) and the dev set with the predictions made by the participant's system:

```
python evaluate.py train.tsv dev.tsv predictions.tsv
```

It needs the train data in order to determine the VID types unseen during training. The script outputs the F1 score for the literal class for all VID types as well as for the unseen VID types. But only the F1 score for all VID types will be used to determine the ranking of the systems.

## Organizers

- [Rafael Ehren](https://www.isi.hhu.de/bereiche-des-institutes/abteilung-fuer-computerlinguistik/unser-team/computerlinguistik?tt_address%5Bfunktion%5D=19133&tt_address%5Bperson%5D=16061&cHash=f19f3068205fd390e30e2dc392ac23bd)
- [Laura Kallmeyer](https://user.phil.hhu.de/kallmeyer/)
- [Timm Lichte](http://timm-lichte.de/)
- [Jakub Waszczuk](https://user.phil.hhu.de/~waszczuk/)
