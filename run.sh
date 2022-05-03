#!/bin/bash

set -e

lang=$1

case $lang in

    C)       cd $lang; make run;;
    C++)     cd $lang; make run;;
    C#)      cd $lang; make run;;
    Clojure) cd $lang; make run;;
    Elixir)  cd $lang; make run;;
    Erlang)  cd $lang; make run;;
    Go)      cd $lang; make run;;
    Groovy)  cd $lang; make run;;
    Haxe)    cd $lang; make run;;
    Java)    cd $lang; make run;;
    Julia)   cd $lang; make run;;
    Perl)    cd $lang; make run;;
    PHP)     cd $lang; make run;;
    Python)  cd $lang; make run;;
    Ruby)    cd $lang; make run;;
    Rust)    cd $lang; make run;;
    Swift)   cd $lang; make run;;

    "")    echo "help: invoke ./run.sh <lang-folder>";;
    *)     echo "unsupported lang $lang";;

esac
