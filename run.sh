#!/bin/bash

lang=$1

case $lang in

    C)     cd $lang; make run;;
    C++)   cd $lang; make run;;
    C#)    cd $lang; make run;;
    Java)  cd $lang; make run;;
    Go)    cd $lang; make run;;
    Swift) cd $lang; make run;;

    "")    echo "help: invoke ./run.sh <lang-folder>";;
    *)     echo "unsupported lang $lang";;

esac
