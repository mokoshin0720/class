#!/bin/sh

concat() {
    PREFECTURE=$1
    STATION=$2
    YEAR=$3
    MONTH=$4

    (head -1 csv/$PREFECTURE/"$YEAR""$MONTH"_"$PREFECTURE"_"$STATION".csv;
        nkf csv/$PREFECTURE/*_$STATION.csv | grep -v S02) > "$YEAR"_"$STATION".csv
}

concat 15 15201060 2020 01