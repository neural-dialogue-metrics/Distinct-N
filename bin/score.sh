#!/usr/bin/env bash

HYPO=/home/cgsdfc/UbuntuDialogueCorpus/ResponseContextPairs/ModelPredictions/VHRED/First_VHRED_BeamSearch_5_GeneratedTestResponses.txt_First.txt
DIR=/home/cgsdfc/Result/Test

python bin/distinct_metric.py --output_dir $DIR $HYPO -n 3
