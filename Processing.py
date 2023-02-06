import os
import pandas as pd

print(os.getcwd())
files = os.listdir()
set = {}
for file in files:


    if file == 'csv':

        new_path = os.path.join(os.getcwd(),file)


        for dataset in os.listdir(new_path):

            head,sep,tail = dataset.partition('.')
            #print(head)
            data = pd.read_csv(os.path.join(new_path,dataset))
            set[head] = data
print(set)





