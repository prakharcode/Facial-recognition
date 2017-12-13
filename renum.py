import os

path = os.getcwd()+'/dataset/kejriwal/'
dirs = os.listdir(path)
for i,item in enumerate(dirs):
    os.rename(path+item,path+'kejriwal'+str(i)+'.jpg')
dirs = os.listdir(path)
