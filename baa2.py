import os

k=0

for root, dirs, files in os.walk('output', topdown=False):
    for f in files:
        temp = os.path.join(root, f)
        temp2 = temp.split('\\')[1].strip('.txt')
        doc = open(os.path.join(root, f), 'r', encoding='utf-8')
        cuis = []
        for line in doc:
            k+=1

print(k)
