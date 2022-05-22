#!/bin/sh

file_count() {
    ls csv/*/*.csv | wc -l
}

file_count_by_station() {
    PREFECTURE=$1
    STATION=$2
    cat csv/$PREFECTURE/*_$STATION.csv | wc -l
}

head_and_tail_of_data() {
    PREFECTURE=$1
    STATION=$2
    METHOD=$3
    DISPLAY_NUMBER=$4

    cat csv/$PREFECTURE/*_$STATION.csv | $METHOD -$DISPLAY_NUMBER | nkf
}

# file_count
# file_count_by_station 14 14204010
head_and_tail_of_data 14 14204010 tail 5