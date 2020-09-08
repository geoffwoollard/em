import subprocess, os, argparse

parser = argparse.ArgumentParser(description='rename file from basefilename_1.ser to basefilename.ser')
parser.add_argument('--filename', type=str, nargs=1,
                    help='file containing list of .ser file names')
parser.add_argument('--ext', type=str, nargs=1,
                    default='mrc',
                    choices=['mrc','tif'],
                    help='output extension')
parser.add_argument('--info', type=str, nargs=1,
                    help='''
                    1. Make list of files to convert (FILE.txt)
                    2. > python ser2mrc.py --filename FILE.txt
                    ''')
args = parser.parse_args()

filename = args.filename[0]
ext = args.ext[0]

with open(filename) as f:
    files = f.read().split('\n')

for file in files:
    if os.path.exists(file): 
        if file.endswith('.ser'):
            command = ['e2proc2d.py',file,file.replace('.ser','.'+ext)]
            subprocess.call(command)
            
        else: print('File:"%s" does not end with .ser' % file)
    else: print('File:"%s" does not exist' % file)

print('Done')