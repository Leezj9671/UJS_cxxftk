# 建议在中文环境下运行，否则会出现codec错误
import requests
import re

def run(username):
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

    burl = 'http://ujs.91job.gov.cn'
    url = burl + '/contest/answer'
    lurl = burl + '/user/login?referer=/contest/answer&callback=login'
    surl = burl + '/contest/savedata'

    s = requests.session()
    s.post(lurl, data=data, headers=headers)

    # 检测是否已经答完题
    html = s.get(url).text
    score = re.findall('<b><font color="red">(.*?)</font></b>', html)
    if score != []:
        print(username, score[0], score[1])
        return

    # 确认已经答完题后，导入题库开始搞事
    from getdict import ansdict
    cnt = 0
    nxtu = s.get(url).url
    while True:
        html = s.get(nxtu).text

        try:
            tid = re.findall('tid=(\d+)', nxtu)[0]
            title = re.findall('<b><font color="red">(.*?)</font><br/>&nbsp;&nbsp;&nbsp;(.*?)</b>', html, re.S)[0][1]
        except:
            print(username, ' is error')
            return

        data = {'tid': tid}
        cnt += 1

        try:
            ans = ansdict[title.strip()]
            if len(ans) == 1:
                data['value'] = ans
            else:
                data['value[]'] =  list(ans)
        except:
            print(nxtu, ' error')

        s.post(surl, data=data, headers=headers).text

        nxtu = re.findall('<a (.*?) href="(.*?)">下一题</a>', html, re.S)
        if nxtu == []:
            break
        else:
            nxtu = burl + nxtu[0][1].replace('\n', '')

    #交卷啦
    jjurl = re.findall('<a(.*?) href="(.*?)">交(.*?)卷</a>', html, re.S)
    if jjurl != []:
        jjurl = burl + jjurl[0][1]
        html = s.get(jjurl)
    print(username, '答题完毕')
    html = s.get(url).text
    score = re.findall('<b><font color="red">(.*?)</font></b>', html)
    if score != []:
        print(username, score[0], score[1])

if __name__ == '__main__':
    for username in range(123, 123):
        run(str(username))
