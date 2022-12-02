#!/bin/bash
cat day2.txt | while read -r line; do
    lower=$(($(echo $line | cut -d- -f1) - 1))
    upper=$(($(echo $line | cut -d- -f2 | cut -d' ' -f1) - 1))
    char=$(echo $line | cut -d' ' -f2 | cut -d: -f1)
    input=$(echo $line | cut -d' ' -f3)
    [ $(echo ${input:${lower}:1}${input:${upper}:1} | grep -o ${char} | wc -l) -eq 1 ] && echo "${line}"
done | wc -l