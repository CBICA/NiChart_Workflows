#! /bin/bash +x

## Function to run dlmuse on study data
##  - Input: all images in input folder
##  - Output: final dlmuse csv for all images

echo "--------------"
echo "Running: $0 $@"

## Read out file and first input file
std=$1
fout=$2
fin1=$3

## Get input and output folder names
din=$(dirname $fin1)
dout=$(dirname $fout)

####################
## Run DLMUSE

## FIXME: Placeholder code (creates fake output files)

##dlmuse ${din} ${dout}         ## Actual call to dlmuse

for fname in `ls -1 ${din}/*.nii.gz`; do
    fbase=$(basename $fname)
    touch ${dout}/${fbase%.nii.gz}_DLMUSE.nii.gz
    echo '''MRID,ROI1,ROI2,ROI3
A,1,2,3''' > ${dout}/${fbase%.nii.gz}_DLMUSE.csv
done

####################
## Combine csv files
for fname in $(ls -1 ${dout}/*_DLMUSE.csv); do
    if [ ! -e $fout ]; then
        cat $fname > $fout
    else
        sed 1d $fname >> $fout
    fi
done
