#!/usr/bin/python

import shutil, os, argparse

parser = argparse.ArgumentParser(description='rename file from basefilename_1.ser to basefilename.ser')
parser.add_argument('--filename', type=str, nargs=1,
                    help='file containing list of _1.ser file names')
args = parser.parse_args()

filename = args.filename[0]

with open(filename) as f:
    files = f.read().split('\n')

for file in files:
    if os.path.exists(file): 
    	if file.endswith('_1.ser'):
    		shutil.move(file,file.replace('_1.ser','.ser'))
    	else: print('File:%s does not end with _1.ser' % file)
    else: print('File:%s does not exist' % file)