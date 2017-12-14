#import the filenames
import glob
allFiles = glob.glob('*.txt')
print(allFiles)

rt = open('000rtttl.py','a')
rt.write('songdict = {')
rt.close()

for i in allFiles:
    songname = i.replace(".txt","")
    #print(songname)
    f = open(i,'r')
    try:
        rtttl = f.read()
        f.close()
        rtttl = rtttl.rstrip()
        #print(rtttl)
        fileText = "\n\"" + songname + "\":\"" + rtttl + "\","
        #print(fileText)
        rt = open('000rtttl.py','a')
        rt.write(fileText)
        rt.close()
    except:
        print("Ooops")
        
rt = open('000rtttl.py','a')
rt.write('\n}')
rt.close()
