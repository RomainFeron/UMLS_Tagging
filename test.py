from difflib import SequenceMatcher as match
from class_Mail import Mail

mail = Mail('ressources/mails/bioinfo_2014-01/1.recoded')
body = mail.body
query = 'gène'
pos = []
scores = []
i = 0
acceptanceThreshold = 0.9

while i+len(query) <= len(body):
    s = match(None, query, body[i:i+len(query)]).ratio()
    if s > acceptanceThreshold:
        if len(pos) > 0 and pos[-1] > i - len(query):
            if scores[-1] <= s:
                scores[-1] = s
                pos[-1] = i
        else:
            scores.append(s)
            pos.append(i)
    i += 1

print(scores)
print(pos)
print(body[pos[0]:pos[0]+len(query)])
