#!/bin/bash
source env/bin/activate
DIRECTORY=$1
aux=`mktemp`
for json in `find $1 -name "*.RAW.json"`;
do
    base=`echo $json| sed 's/RAW.json$//'`
    patch=$base"patch"
    script="python -m yabormeparser.parser2 -i "$json
    if [ -f $patch ];
    then
        script="$script -p $patch"
    fi
    echo $script >> $aux
done
cat $aux | parallel -j 8
RAW=`find $DIRECTORY/ -name "*.RAW.json" | wc -l`
JSON=`find $DIRECTORY/ -name "*.json" | grep -v RAW| wc -l`
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
