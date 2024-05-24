#! /bin/bash +x

## Function to combine individual csv files with MUSE ROI values
##  - Discards the header from all files, except the first one

## Read out file and first input file
fout=$1
fin1=$2

## Shift args to other input files
shift;
shift;

## Write first file to output
cat $fin1 > $fout

## Add the data line from all other files to the output
for fcurr in "$@"; do
    tail -1 $fcurr
done >> $fout
