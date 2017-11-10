#!/bin/bash
if [ $# -ne 1 ]; then
  echo 'Usage: $0 year'
  exit
fi
if [ -d $1 ]; then
rm -rf $1
fi
mkdir ./$1
for x in {January,February,March,April,May,June,July,August,Sepetember,October,November,December}; do
mkdir ./$1/$x
case $x in
  January|March|May|July|August|October|December)
    for a in $(seq 31);do
      touch $1/$x/$a
    done
    ;;
  April|June|Sepetember|November)
    for a in $(seq 30);do
      touch $1/$x/$a
    done
    ;;
  February)
    if ! (($1 % 4)); then
      for a in $(seq 29);do
        touch $1/$x/$a
      done
    else
      for a in $(seq 28);do
        touch $1/$x/$a
      done
    fi
  ;;
esac
done

