from collections import Counter

def splitbar(ent):
    a=dict(Counter(ent))
    if a['*']>=2:
        print('*가 여러개 들어가 있는것 같군요')
    else:
        sb=ent.split('|')
        for i in sb:
            if '*' in i:
                print('*')
            else:
                print('|'+i)

splitbar(input())