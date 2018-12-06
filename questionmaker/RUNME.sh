#!/bin/bash
quesDir="${PWD}/myquestions"
htmlDir="${PWD}/build"
quesJS="${PWD}/questions.js"

if [ -z $1 ]; then
    python3 addq.py ${quesDir}/*
elif [ $1 == "-h" ]; then
    echo "Usage: `basename $0` [option...]"
    echo "   -c, --clean        remove built html files"
    exit 0
elif [ $1 == "--help" ]; then
    echo "Usage: `basename $0` [option...]"
    echo "   -c, --clean        remove built html files"
    exit 0
elif [ $1 == "--clean" ]; then
    echo "removing all html files..."
    rm ${htmlDir}/*
    echo "" > ${quesJS}
    echo "Done"
elif [ $1 == "-c" ]; then
    echo "removing all html files..."
    rm ${htmlDir}/*
    echo "" > ${quesJS}
    echo "Done"
fi
