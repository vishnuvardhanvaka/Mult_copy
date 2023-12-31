import os
import glob
from tqdm import tqdm
import time

def getpath(f):
	tf=[f'{f}/*.jpg',f'{f}/*.zip',f'{f}/*.png',f'{f}/*.pdf',f'{f}/*.otf',f'{f}/*.ttf',f'{f}/*.mp3',f'{f}/*.mp4']
	
	dirs=os.listdir(f)
	dirs=[f'{f}/{item}' for item in dirs]
	
	files = [file for t in [glob.glob(e) for e in tf] for file in t]
	dirs=[dir for dir in dirs if dir not in files and '.' not in dir]
	
	for dir in dirs:
		rt=getpath(dir)
		if len(rt)!=0:
			files+=rt
	return files
	
def getdict(files):
	d={}
	for file in files:
		filename=file.split('/')[-1]
		if filename not in d:
			d[filename]=file
	return d
	
def createdir(d,savepath):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	bar=tqdm(total=len(d),unit='file')
	for filename in d:
		with open(d[filename],'rb') as f1, open(f'{savepath}/{filename}','wb') as f2:
			data=f1.read()
			f2.write(data)
		time.sleep(0.1)
		bar.update(1)
	bar.close()	
	print('Successfully files copied !')

folder='ALL FONTS'
save_as='EX FILES'
print('Starting ...')
files=getpath(folder)
print(f'{len(files)} files detected ...')
d=getdict(files)
st=createdir(d,save_as)
