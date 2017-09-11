# encoding=utf-8
import requests
import re
headers = {
    # 自行修改
    'Cookie': 'UM_distinctid?????????QAQ???????wangjishanle59124444-1505101164-http%253A%252F%252Fujs.91job.gov.cn%252F%7C1505117383; PHPSESSID2=taqp5pjj99llgli1dour6t4nc1',
}
bt = 100
url = 'http://ujs.91job.gov.cn/contest/question?page='
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
