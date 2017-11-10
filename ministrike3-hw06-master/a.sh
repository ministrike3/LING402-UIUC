#!/bin/bash
if [ $# -ne 1 ]; then
  echo 'Usage: $0 year'
  exit
fi
if [ -d $1 ]; then
rm -rf $1
fi

if [ ${#1} -ne 4 ]; then
  echo 'Usage: $0 year'
  exit
fi

if ! [[ $1 =~ ^[0-9]+$ ]]; then
   echo 'Usage: $0 year'
  exit
fi
mkdir ./$1

for x in {January,February,March,April,May,June,July,August,Sepetember,October,November,December}; do
mkdir ./$1/$x
case $x in
  January|March|May|July|August|October|December)
    for a in $(seq 31);do
      wget -O $1/$x/$a "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
    done
    ;;
  April|June|Sepetember|November)
    for a in $(seq 30);do
      wget -O $1/$x/$a "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
    done
    ;;
  February)
    if ! (($1 % 400)); then
      for a in $(seq 29);do
        wget -O $1/$x/$a  "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
      done
    elif ! (($1 % 100)); then
      for a in $(seq 28);do
        wget -O $1/$x/$a "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
      done
    elif ! (($1 % 4)); then
      for a in $(seq 29);do
        wget -O $1/$x/$a "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
  	done
    else
      for a in $(seq 28);do
        wget -O $1/$x/$a "http://en.wikipedia.org/w/index.php?title=$x_$a&printable=yes"
      done
    fi
  ;;
esac
done
