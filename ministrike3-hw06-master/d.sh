#!/bin/bash
if [ -d $1 ]; then
rm -rf $1
fi

mkdir ./$1
for x in {January,February,March,April,May,June,July,August,Sepetember,October,November,December}; do
mkdir ./$1/$x
done 


