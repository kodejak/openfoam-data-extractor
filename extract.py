#!/usr/bin/python

# File:     extract.py
# Author:   kodejak <mail at kodejak dot de>
#
# Usage:    "python extract.py -s <searchpattern> (e.g. centreOfMass)
#               -f <filename> (e.g. sixDoFRigidBodyMotionState)
#               -v (verbose screen output)"
#
# Info:
#           This script extracts searched datas from the OpenFOAM project
#           generated files e.g. gravity, centreOfMass etc. The datas will be
#           stored as a CSV file located at the directory of the script, named
#           like the command line search pattern. This file can be easily
#           imported to OpenOffice calc, Matlab or whatever.
#
# Copyright (C) 2015  Christian Handorf
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
##

import os, os.path
import time
import sys, getopt

files_array = []
sorted_map = {}
screen_verbose = 0

usage_str = """Usage:\r\nextract.py -s <searchpattern> (e.g. centreOfMass)
                -f <filename> (e.g. sixDoFRigidBodyMotionState)
                -v (verbose screen output)"""

# Find string between two characters
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# Recursely find all files with "file_name" and put it in an array
def searchdatafiles(directory, file_name):
    global files_array
    for root, dirs, files in os.walk(directory):
        for f in files:
            fullpath = os.path.join(root, f)
            base=os.path.basename(fullpath)
            f_name = os.path.splitext(base)[0]
            if f_name.lower() == file_name.lower():
                files_array.append(fullpath)

# Sort founded datas and dump it to a csv file
def sortanddump(fname, amap):
    with open(fname + ".csv", "w") as myfile:
        myfile.write("")
        
    for key in sorted(amap):
        with open(fname + ".csv", "a") as myfile:
            myfile.write(key + ';' + amap[key] + '\r\n')
            if screen_verbose == 1:
                print "Step " + key, amap[key]

# Search in founded files array for patterns like "centreOfMass" or "gravity"
def searchinfiles(search_pattern):
    dir_name = ''
    extract = ''
    global files_array                    
    for idx, filename in enumerate(files_array):
        with open(files_array[idx]) as input_file:
            for x, line in enumerate(input_file):
                if search_pattern in line:
                    dir_name = os.path.abspath(os.path.join(filename, os.pardir))
                    dir_name = os.path.abspath(os.path.join(dir_name, os.pardir))
                    dir_name = os.path.basename(os.path.normpath(dir_name))
                    extract = find_between(line, "(", ")")
                    extract = extract.strip()
                    extract = extract.replace(' ', ';')
                    sorted_map[dir_name] = extract

def main(argv):
    search_patt = ''
    file_name = ''
    files_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hf:s:v")
    except getopt.GetoptError:
        print usage_str
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print usage_str
            sys.exit()
        elif opt in ("-s"):
            search_patt = arg
        elif opt in ("-f"):
            file_name = arg
        elif opt in ("-v"):
            global screen_verbose
            screen_verbose = 1
    
    if search_patt == '':
        print usage_str
        sys.exit(2)
    if file_name == '':
        print usage_str
        sys.exit(2)
    
    files_dir = os.getcwd()
    searchdatafiles(files_dir, file_name)
    searchinfiles(search_patt)
    sortanddump(search_patt, sorted_map)
    print "DONE!"


if __name__ == "__main__":
   main(sys.argv[1:])
