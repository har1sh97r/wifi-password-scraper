import os
from time import sleep
import xml.etree.ElementTree as ET
import json
import shutil

if not os.path.exists('./data/'):
  os.mkdir('./data/')

# os.system('cmd /c "netsh wlan export profile folder=.\\data\ key=clear"')
os.popen("netsh wlan export profile folder=.\\data\ key=clear")

sleep(1)

dir_path = r'data'
file_count = 0
dir_lst=[]
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        dir_lst.append('.\\'+dir_path+'\\'+path)
        file_count += 1
print('Total Passwords Found: ', file_count)

data={}
for file in dir_lst:
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        data[file[13:-4]]=root[4][0][1][2].text
    except:
        continue

with open('pwds.json', 'w') as f:
    json.dump(data, f,indent=4)
    print("Saved all the passwords succesfully in the pwds.json file")

try:
    shutil.rmtree('.\data')
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

sleep(3)
