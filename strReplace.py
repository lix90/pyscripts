# batch script for string replace
from os.path import join
from glob import glob

inputDir = 'Desktop'
fileExt = '*.txt'
strOld1 = 'but'
strOld2 = 'shit'
for f in glob(join(inputDir, fileExt)):
    ff = open(f, 'rw').read().replace(strOld1, '').replace(strOld2, '')
    ff2 = open(f, 'w')
    ff2.write(ff)
