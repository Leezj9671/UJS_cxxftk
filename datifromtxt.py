# 应要求做了一个从txt导入做题的功能
# OCR from http://zhcn.109876543210.com/识别图片学号
from dati import run

todoarr = []
with open('todo.txt', 'r') as f:
    todoarr= f.read().splitlines()
    todoarr = list(filter(lambda x: x != '', todoarr))

print(todoarr)
print(len(todoarr))

list(map(run, todoarr))