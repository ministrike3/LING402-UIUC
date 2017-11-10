#!/bin/bash

###############################################################################
# Instructions:
###############
#
# Modify this script so that it accepts text from standard input
#  sorts the input,
#  then performs a uniq, counting the number of times each line occurs.
#
# The results should be printed to standard output in the form:
#
# count\tchildren\tparent
#
###############################################################################

#cat /dev/stdin | sort | uniq -c |tr -s " " "\t" | sed 's/.//'
#cat /dev/stdin | sort | uniq -c |sed 's/[ \t]*//'|awk 'sub(/[[. .]]/, "\t")
cat | sort | uniq -c |sed 's/[ \t]*//1'|sed 's/ /\t/'
