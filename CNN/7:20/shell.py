import os, commands
# commands.getoutput('python cleaning.py')
# commands.getoutput('python intensive_point.py')
# commands.getoutput('python cab.py')
# commands.getoutput('python centroid.py')
# commands.getoutput('python csvtoimage.py')

print commands.getoutput('python create_data.py')
print commands.getoutput('python train.py ')

print commands.getoutput('python check.py ./checkimage/intensive/jyu.png')
print commands.getoutput('python check.py ./checkimage/intensive/kdo.png')
print commands.getoutput('python check.py ./checkimage/intensive/kwk.png')
print commands.getoutput('python check.py ./checkimage/intensive/okd.png')
print commands.getoutput('python check.py ./checkimage/intensive/skr.png')
print commands.getoutput('python check.py ./checkimage/intensive/smd.png')
print commands.getoutput('python check.py ./checkimage/intensive/snd.png')


print commands.getoutput('python check.py ./checkimage/naive/jyu.png')
print commands.getoutput('python check.py ./checkimage/naive/kdo.png')
print commands.getoutput('python check.py ./checkimage/naive/kwk.png')
print commands.getoutput('python check.py ./checkimage/naive/okd.png')
print commands.getoutput('python check.py ./checkimage/naive/skr.png')
print commands.getoutput('python check.py ./checkimage/naive/smd.png')
print commands.getoutput('python check.py ./checkimage/naive/snd.png')
