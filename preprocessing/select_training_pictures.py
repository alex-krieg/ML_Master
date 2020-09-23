from shutil import copyfile
import glob
from os.path import exists

catlist=glob.glob('./data/annotations/*.xml')
for xml in catlist:
    print(xml)
    if exists('./workspace/training_demo/images/train/'+xml[-13:-4]+".jpg"):
        copyfile(xml, "./workspace/training_demo/images/train/"+xml[-13:])
    elif exists('./workspace/training_demo/images/test/'+xml[-13:-4]+".jpg"):
        copyfile(xml, "./workspace/training_demo/images/test/"+xml[-13:])
    else:
        print(xml + ' not found')


