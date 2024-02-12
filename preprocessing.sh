#!/bin/bash
read -p $'Enter №: \n' N
read -p $'Enter letter: \n' l
read -p $'Enter file name: \n' file_name
python /home/natalka/mmp/algo/testing.py
cat output.txt >> "$N$l. $file_name.py"
