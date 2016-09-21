#!/bin/bash
source env/bin/activate
DIRECTORY=$1
aux=`mktemp`
date_begin=`date`
for pdf in `find $1 -name "*.pdf"`;
do
    base=`echo $pdf| sed 's/pdf$//'`
    patch=$base"RAW.patch"
    script="python -m yabormeparser.parser -i "$pdf
    if [ -f $patch ];
    then
        script="$script -p $patch"
    fi
    echo $script >> $aux
done
cat $aux | parallel -j 8
date_end=`date`
PDF=`find $DIRECTORY/ -name "*.pdf" | wc -l`
JSON=`find $DIRECTORY/ -name "*.RAW.json" | wc -l`
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
echo "  End: $date_end"
echo '------------------------'
