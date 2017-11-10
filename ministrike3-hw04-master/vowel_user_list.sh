#!/bin/bash

###############################################################################
# Instructions:
###############
#
# The file /etc/passwd contains (among other things) usernames as well as
#  a default shell for each user.
#
# For most users, the default shell is /bin/bash
#
# The output of this script should be a sorted list of usernames
#   whose default shell is NOT /bin/bash
#   and whose username is exactly four characters long
#   and where the second character in the username is a vowel (a, e, i, o, or u)
#   and where the first, third, and fourth characters are NOT vowels
#
###############################################################################



grep -v "/bin/bash" /etc/passwd | cut -d ':' -f 1  | grep '^[^aeiou][aeiou][^aeiou][^aeiou]$'
