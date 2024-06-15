#! /bin/bash

## Read input
in_csv=$1
in_mdl=$2
out_csv=$3

## Apply combat learn
cmd="neuroharm -a apply -i $in_csv -m $in_mdl -u $out_csv"
echo "About to run: $cmd"
$cmd
