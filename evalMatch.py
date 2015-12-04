import os

os.path.dirname(os.path.abspath(__file__))

# Global variables
ressourcesPath = 'ressources'
# Path to eval files
evalPath = os.path.join(ressourcesPath,'eval','cp_docs')
# Path to output folder
outputPath = 'output'

manual = {}
auto = {}

for root, dirs, files in os.walk('eval\\cp_docs', topdown=False):
    for f in files:
        temp = os.path.join(root, f)
        temp2 = temp.split('\\')[2] + '_' + temp.split('\\')[3].strip('.recoded.eval')
        doc = open(os.path.join(root, f), 'r')
        cuis = []
        for line in doc:
            cuis.append(line.strip('\n'))
        manual[temp2] = cuis

for root, dirs, files in os.walk('output', topdown=False):
    for f in files:
        temp = os.path.join(root, f)
        temp2 = temp.split('\\')[1].strip('.txt')
        doc = open(os.path.join(root, f), 'r')
        cuis = []
        for line in doc:
            lala = line.split('|')
            cuis.append(lala[0])
        auto[temp2] = cuis

shared = {}
onlyManual = {}
onlyAuto = {}

for key in manual:
    shared[key] = 0
    onlyAuto[key] = 0
    onlyManual[key] = 0
    for value in manual[key]:
        if value in auto[key]:
            shared[key] += 1
        else:
            onlyManual[key] += 1
    for value in auto[key]:
        if value not in manual[key]:
            onlyAuto[key] += 1

print(shared)
print(onlyAuto)
print(onlyManual)

outputfile = open('baa.txt', 'w')
for key in shared:
    outputfile.write(key + ',' + str(shared[key]) + ',' + str(onlyAuto[key]) + ',' + str(onlyManual[key]) + '\n')

