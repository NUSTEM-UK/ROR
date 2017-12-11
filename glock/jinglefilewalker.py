#import the filenames
import glob
filenames = glob.glob('xmassongs/*.bas')

songdict ={}

# walk through the files
for i in filenames:
    # create the key and adjust the filename
    namestore = i.replace('xmassongs/',"")
    i = i.replace('xmassongs/',"")
    i = i.rstrip('.bas')
    if i[-1] in ["1","2","3"]:
        i = i[:-1]
    i = i.lower()
    i = i.split()
    # store in the song dictionary
    songdict[namestore]=i