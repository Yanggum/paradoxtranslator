# -*- coding: utf-8 -*-
import glob
import re
from googletrans import Translator

translator = Translator()

path = 'C:\\Users\\Scret\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\oldworldblueskorean\\localisation\\'
fileName = '*'
extension = '.yml'
srcFile = path + fileName + extension


files = glob.glob(srcFile)

for file in files:    
    f = open(file, 'rt', encoding='UTF8')
    fileArr = file.split('\\');
    fileArr = fileArr[len(fileArr)-1].split('.')[0];
    destFile = path + fileArr + '_dest' + extension
    wf = open(destFile, 'wt', encoding='UTF8')
      
    while True:
        line = f.readline()

        if not line: 
            break
    
        x = re.findall(r'\"(.+)\"', line)
        if translator.detect(x).lang == 'ko':
            
        if len(x) > 0:
            translatedText =  '"' + translator.translate(x[0], dest='ko', src='en').text + '"'
            line = re.sub(r'\"(.+)\"', translatedText, line);
            print(line)
       
       
        wf.write(line)        
        
        
    f.close()        
    wf.close()
