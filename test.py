l = [['genet','ENG','C0325074'],['gene','ENG','C0017337'], ['geng-tang','ENG','C0670194']]

def getKey(item):
    return item[0]

fT = sorted(l,key = getKey)
print(fT)
