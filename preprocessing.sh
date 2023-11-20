#!/bin/bash
python /home/ubuntu/mmp/algo/testing.py
read -p $'Enter file name: \n' file_name
cat output.txt >> "$file_name.py"
