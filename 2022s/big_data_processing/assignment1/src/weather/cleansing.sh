#!/bin/sh

cleansing() {
    SOURCE_FILE=$1
    OUTPUT_FILE=$2
    (nkf $SOURCE_FILE.csv | grep "年月日" | nkf -s; tail -365 $SOURCE_FILE.csv) > $OUTPUT_FILE.csv
}

cleansing tsujidou weather