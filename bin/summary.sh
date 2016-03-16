DIR=$1
echo "Files"
echo "-----"
TOT=`find $DIR -name "*RAW.json"|wc -l`
OK=`find $DIR -name "*.json"|grep -v RAW|wc -l`
ERR=`find $DIR -name "*.TMP"|grep -v RAW|wc -l`
FAIL=`echo $TOT - \( $ERR + $OK \) | bc`
echo "TOTAL: " $TOT
echo "OK:    " $OK
echo "ERROR: " $ERR
echo "FAIL:  " $FAIL
echo
echo "Errors by type"
echo "--------------"
grep \"error\" $DIR -Rh|sed 's/       "error": "//'| sed 's/",//' \
    | sort |uniq -c|sort -nr|sed "s/    /*/"
echo
