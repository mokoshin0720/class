#!/bin/sh

word_count() {
    FILE=$1
    wc -l $FILE.csv
}

head_and_tail_of_data() {
    FILE=$1
    METHOD=$2

    nkf $FILE.csv | $METHOD
}

word_count tsujidou
head_and_tail_of_data weather tail