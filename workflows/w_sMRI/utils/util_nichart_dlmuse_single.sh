#!/bin/sh +x

fin=$1
fout=$2
foutcsv=$3

## FIXME: Placeholder function (creates fake output files)

# mkdir $(dirname $fout) -pv

touch $fout
echo '''MRID,ROI1,ROI2,ROI3
A,1,2,3''' > $foutcsv
