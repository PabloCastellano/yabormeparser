DIR=$1
find $DIR -name "*patch.TMP" | xargs rm
find $DIR -name "*json" | xargs rm
