#!/bin/bash
cat day2.txt | while read -r line; do
    lower=$(echo $line | cut -d- -f1)
    upper=$(echo $line | cut -d- -f2 | cut -d' ' -f1)
    char=$(echo $line | cut -d' ' -f2 | cut -d: -f1)
    count=$(echo $line | cut -d' ' -f3 | grep -o ${char} | wc -l)
    [ ${count} -le ${upper} ] && [ ${count} -ge ${lower} ] && echo "match"
done | wc -l