#!/usr/bin/env bash
find . -name "*patch.TMP" | sed 's/\(.*\).TMP$/cp \1\.TMP \1/' | sh
for f in `find -name "*patch"`
do
    if [[ $f == *"RAW"* ]]
    then
        p=`echo $f | sed 's/\(.*\)RAW.patch$/\1pdf/'`
        emacs $f & evince $p
    else
        p=`echo $f | sed 's/\(.*\)patch$/\1RAW.json/'`
        emacs $f $p
    fi
done
