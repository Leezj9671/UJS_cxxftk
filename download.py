import requests
import re

from config import burl

headers = {
    # 自行修改
    'Cookie': 'your cookie',
}

url = burl +　'/contest/question?page='
with open('tiku.txt', 'w') as f:
    f.write('github.com/leezj9671\n')
    for i in range(1, 729):
        r = requests.get(url + str(i), headers=headers).content
        r = r.decode('utf-8')
        title = re.findall('<b><font color="red">(.*?)</font><br/>&nbsp;&nbsp;&nbsp;(.*?)</b>', r, re.S)
        choices = re.findall('<label>(.*?)</label>', r, re.S)
        answer = re.findall('<p><font color="red"><b>(.*?)</b></font></p>', r)[0]
        f.write('\n'.join(title[0]) + '\n')
        f.write('\n'.join(choices) + '\n')
        f.write(answer + '\n\n')
