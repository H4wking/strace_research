#!/bin/bash

C=0

while getopts ":p:f:c" opt
do
  case $opt in
  p ) 
    PROCESS=$OPTARG
    ;;
  f )
    FILE=$OPTARG
    ;;
  c )
    C=1
    ;;
  *)
    exit 2
    ;;

  esac
done


PS=$(ps -C "$PROCESS")
PSARRAY=($PS)
PID=${PSARRAY[4]}

if [ $C -eq 1 ]
then
  sudo strace -c -p "$PID" -o "$FILE"
else
  sudo strace -p "$PID" -o "$FILE"
fi
