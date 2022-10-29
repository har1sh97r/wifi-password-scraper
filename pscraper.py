import os
from time import sleep
import xml.etree.ElementTree as ET
import json
import shutil

if not os.path.exists('./data/'):
  os.mkdir('./data/')
  
os.popen("netsh wlan export profile folder=.\\data\ key=clear")

sleep(1)

dir_path = r'data'
file_count = 0
data={}
#dir_lst=[]
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        try:
            tree = ET.parse(os.path.join(dir_path, path))
            root = tree.getroot()
            print(path)
            data[os.path.join(path[6:-4])]=root[4][0][1][2].text
            file_count += 1
        except:
            continue
        
print('Total Passwords Found: ', file_count)

with open('pwds1.json', 'w') as f:
    json.dump(data, f,indent=4)
    print("Saved all the passwords succesfully in the pwds.json file")

try:
    shutil.rmtree('.\data')
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
sleep(3)
