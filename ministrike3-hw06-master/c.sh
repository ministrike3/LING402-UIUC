#!/bin/bash
if [ -d $1 ]; then
rm -rf $1
fi

mkdir ./$1
for x in {January,February,March,April,May,June,July,August,Sepetember,October,November,December}; do
mkdir ./$1/$x
case $x in
  January)
    for a in $(seq 31);do
      touch $1/$x/$a
    done
    ;;
  February)
    for a in $(seq 28);do
      touch $1/$x/$a
    done
  ;;
  March)
    for a in $(seq 31);do
      touch $1/$x/$a
    done
  ;;
  April)
    for a in $(seq 30);do
      touch $1/$x/$a
    done
  ;;
  May)
    for a in $(seq 31);do
      touch $1/$x/$a
    done
  ;;
  June)    for a in $(seq 30);do
        touch $1/$x/$a
      done
      ;;
  July)    for a in $(seq 31);do
        touch $1/$x/$a
      done
      ;;
  August)    for a in $(seq 31);do
        touch $1/$x/$a
      done
      ;;
  Sepetember)    for a in $(seq 30);do
        touch $1/$x/$a
      done
      ;;
  October)    for a in $(seq 31);do
        touch $1/$x/$a
      done
      ;;
  November)    for a in $(seq 30);do
        touch $1/$x/$a
      done
      ;;
  December)    for a in $(seq 31);do
        touch $1/$x/$a
      done
      ;;
esac
done






