#!/bin/bash
source ~/.virtualenvs/yabormeparser/bin/activate

set -u

DIRECTORY_IN=$1
DIRECTORY_OUT=$2
aux=`mktemp`
date_begin=`date`

mkdir -p $DIRECTORY_OUT

for pdf in `find $DIRECTORY_IN -name "*.pdf"`;
do
    base=`echo $pdf| sed 's/pdf$//'`
    patch=$base"RAW.patch"
    script="python -m yabormeparser.parser -i $pdf -o $DIRECTORY_OUT"
    if [ -f $patch ];
    then
        script="$script -p $patch"
    fi
    echo $script >> $aux
done
date_begin2=`date`
cat $aux | parallel -j 8
date_end=`date`
PDF=`find $DIRECTORY_IN/ -name "*.pdf" | wc -l`
JSON=`find $DIRECTORY_OUT/ -name "*.RAW.json" | wc -l`
ERROR=`echo $PDF - $JSON | bc`
echo PDFs $PDF
echo JSONs $JSON
echo ERRORs $ERROR
echo '------------------------'
if [ $PDF = $JSON ]; then
    echo 'OK! PDF files = JSON files'
else
    echo 'FAIL! PDF files != JSON files'
fi
echo '------------------------'
echo "TIME SPENT:"
echo "  Start: $date_begin"
echo "  Parsing start: $date_begin2"
echo "  End: $date_end"
echo '------------------------'
