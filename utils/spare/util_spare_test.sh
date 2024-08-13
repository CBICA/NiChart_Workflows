#! /bin/bash

# download spare package
echo "Downloading spare score package..."
if [ -d "/spare_score" ]
then
    echo "spare score clone already exists!"
else
    git clone https://github.com/CBICA/spare_score.git
fi
python setup.py bdist_wheel
cd dist
WHEEL_FILE=$(ls spare_scores*)
pip install "$WHEEL_FILE"
cd ..
echo "spare score is downloaded!"

## Read input
in_csv=$1
in_mdl=$2
stype=$3
out_csv=$4

## Apply spare test
cmd="spare_score -a test -i $in_csv -m $in_mdl -o ${out_csv%.csv}_tmpout.csv"
echo "About to run: $cmd"
$cmd

## Change column name, remove first (index) column
sed "s/SPARE_score/SPARE${stype}/g" ${out_csv%.csv}_tmpout.csv | cut -d, -f2- > $out_csv
rm -rf ${out_csv%.csv}_tmpout.csv
