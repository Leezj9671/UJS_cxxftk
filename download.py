import requests
import re

from config import burl

# 登陆
s = requests.session()
username = '3140604015'
password = username[-6:] if username else ''
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",

}
data = {
    'username': username,
    'university': '',
    'loginType': 'normal',
    'password': password,
    'loginsubmit': '1',
}
purl = burl + '/contest/question?page='
lurl = burl + '/user/login?referer=/contest/answer&callback=login'
s.post(lurl, data=data, headers=headers)

with open('tiku.txt', 'w') as f:
    f.write('github.com/leezj9671\n')
    for i in range(1, 729):
        r = s.get(purl + str(i), headers=headers).text
        r = re.search('<div class="all">(.*)</div>', r, re.S).group()
        r = r.encode('gbk', 'ignore').decode('gbk')
        title = re.findall('<b><font color="red">(.*?)</font><br/>&nbsp;&nbsp;&nbsp;(.*?)</b>', r, re.S)
        choices = re.findall('<label>(.*?)</label>', r, re.S)
        answer = re.findall('<p><font color="red"><b>(.*?)</b></font></p>', r)[0]
        title = list(title[0])
        print(title, choices, answer)
        f.write('\n'.join(title) + '\n')
        f.write('\n'.join(choices) + '\n')
        f.write(answer + '\n\n')
