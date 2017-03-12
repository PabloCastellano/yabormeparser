#!/bin/bash
set -u

DIR=$1
find $DIR -name "*patch.TMP" | xargs rm
find $DIR -name "*json" | xargs rm
find $DIR -name "*json.?" | xargs rm
