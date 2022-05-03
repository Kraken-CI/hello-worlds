#!/bin/bash

set -e

lang=$1

case $lang in

    C)       cd $lang; make all;;
    C++)     cd $lang; make all;;
    C#)      cd $lang; make all;;
    Clojure) cd $lang; make all;;
    Dart)    cd $lang; make all;;
    Elixir)  cd $lang; make all;;
    Erlang)  cd $lang; make all;;
    Go)      cd $lang; make all;;
    Groovy)  cd $lang; make all;;
    Haskel)  cd $lang; make all;;
    Haxe)    cd $lang; make all;;
    Java)    cd $lang; make all;;
    Julia)   cd $lang; make all;;
    Perl)    cd $lang; make all;;
    PHP)     cd $lang; make all;;
    Python)  cd $lang; make all;;
    Ruby)    cd $lang; make all;;
    Rust)    cd $lang; make all;;
    Swift)   cd $lang; make all;;

    "")    echo "help: invoke ./run.sh <lang-folder>";;
    *)     echo "unsupported lang $lang";;

esac
