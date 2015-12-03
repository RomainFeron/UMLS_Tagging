import difflib
from class_Mail import Mail

mail = Mail('ressources/mails/bioinfo_2014-01/1.recoded')
body = mail.body
query = 'Bioinformatics'
query = 'Stupidstuff'


seq=difflib.SequenceMatcher(None,query,body)
d=seq.ratio()
print (d)

