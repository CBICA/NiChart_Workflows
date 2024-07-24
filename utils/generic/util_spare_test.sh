#! /bin/bash

## Read input
in_csv=$1
in_mdl=$2
out_csv=$3

## Apply spare test
cmd="spare_score -a test -i $in_csv -m $in_mdl -o $out_csv"
echo "About to run: $cmd"
$cmd

