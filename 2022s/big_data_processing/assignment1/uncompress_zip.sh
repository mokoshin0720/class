#!/bin/sh

uncompress() {
    SAVE_DIRECTORY=$1
    DATA_DIRECTORY=$2

    mkdir $SAVE_DIRECTORY
    
    for f in $DATA_DIRECTORY/*.zip
        do unzip $f -d data
    done
}

uncompress csv data