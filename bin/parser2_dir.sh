#!/bin/bash
source ~/.virtualenvs/yabormeparser/bin/activate

set -u

DIRECTORY_IN=$1
DIRECTORY_OUT=$2
aux=`mktemp`
date_begin=`date`

mkdir -p $DIRECTORY_OUT

for json in `find $DIRECTORY_IN -name "*.RAW.json"`;
do
    base=`echo $json| sed 's/RAW.json$//'`
    patch=$base"patch"
    script="python -m yabormeparser.parser2 -i $json -o $DIRECTORY_OUT"
    if [ -f $patch ];
    then
        script="$script -p $patch"
    fi
    echo $script >> $aux
done
date_begin2=`date`
cat $aux | parallel -j 8
date_end=`date`
RAW=`find $DIRECTORY_IN/ -name "*.RAW.json" | wc -l`
JSON=`find $DIRECTORY_OUT/ -name "*.json" | grep -v RAW| wc -l`
ERROR=`echo $RAW - $JSON | bc`
echo RAWs $RAW
echo JSONs $JSON
echo ERRORs $ERROR
echo '------------------------'
if [ $RAW = $JSON ]; then
    echo 'OK! JSON files = RAW files'
else
    echo 'FAIL! JSON files != RAW files'
fi
echo '------------------------'
echo "TIME SPENT:"
echo "  Start: $date_begin"
echo "  Parsing start: $date_begin2"
echo "  End: $date_end"
echo '------------------------'
