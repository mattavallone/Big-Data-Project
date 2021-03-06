#!/usr/bin/env python
# coding: utf-8

# The purpose of this script is to read in a list of dataset json files and merge them into a single task1.json

import os
import json

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('{ "predicted_types": [')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(infile.read())
        outfile.write('] }')

if __name__ == "__main__":
    
    output = "task2.json"
    files = []
    directory = "/home/mva271/"

    for file in os.listdir(directory):
        if(file != 'cluster1.txt' and file != 'task2.py' and file != 'run_task2.sh' and file != 'merge_jsons.py'):
            files.append(directory+str(file))

    cat_json(directory+output, files)