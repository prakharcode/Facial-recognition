import os
import md5
size_file = {}
path = './dataset/'
for dirs in os.listdir(path):
    size = os.path.getsize(path+dirs)
    if size_file.has_key(size):
        size_file[size].append(path+dirs)
    else:
        size_file[size]=[]
        size_file[size].append(path+dirs)
        hashes = {}
for key in size_file:
    if len(size_file[key])>1:
        for i in size_file[key]:
            m = md5.new(open(i,'rb').read())
            if hashes.has_key(key):
                if hashes[key].has_key(m.digest()):
                    hashes[key][m.digest()].append(i)
                else:
                    hashes[key][m.digest()]=[i]
            else:
                hashes[key]={m.digest():[i]}
for key in hashes:
    for an_key in hashes[key]:
        if len(hashes[key][an_key])>1:
            print "DUPLICATES" ,hashes[key][an_key]


for key in hashes:
    for an_key in hashes[key]:
        if len(hashes[key][an_key])>1:
            for i in hashes[key][an_key][1:]:
                print "Removing...",i
                os.remove(i)
