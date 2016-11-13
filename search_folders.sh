#!/bin/bash

search_term=$1
default_folder=/home/jef/search/1st_test/

if [ -z "$2" ]
then
	default_folder=$2
fi

grep -rin $search_term $default_folder | awk '{print $1}' | cut -f1 -d":" | sort | uniq | while read -r line ; do
	elinks $line | less
done
