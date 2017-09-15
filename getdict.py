import re

findans = False
istitle = False
ansdict = {}
title = ''
with open('tiku.txt', 'r') as f:
    for line in f.readlines():
        if istitle:
            title = line.strip()
            istitle = False
            continue
        if findans:
            ans = re.findall('正确答案:(\w+)', line)
            if ans != []:
                ansdict[title] = ans[0]
                findans = False
        else:
            t = re.match('第(\d+)题', line)
            if t:
                findans = True
                istitle = True
