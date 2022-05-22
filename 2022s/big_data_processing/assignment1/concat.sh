#!/bin/sh

concat() {
    PREFECTURE=$1
    STATION=$2
    YEAR=$3
    MONTH=$4

    (head -1 csv/$PREFECTURE/"$YEAR""$MONTH"_"$PREFECTURE"_"$STATION".csv;
        nkf csv/$PREFECTURE/*_$STATION.csv | grep -v SO2) > "$YEAR"_"$STATION".csv
}

concat 14 14204010 2020 01