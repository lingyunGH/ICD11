#-*-coding=utf-8-*-
import pandas as pd
import re
exl = pd.read_excel('ICD11.xls')

bianma = list(exl['国际ICD11编码'])

regex1 = re.compile('\+')
regex2 = re.compile('/')
regex3 = re.compile('\*')
fatherNode1 = []
fatherNode2 = []
for bm in bianma:
    #两个父节点
    if regex1.findall(bm):
        node = bm.split('+')
        #第一个父节点
        fatherNode1.append(node[0].split('.')[0])
        #第二个父节点
        if node[1]:
            fn2 = node[1].split('.')[0]
            if regex3.findall(fn2):
                fatherNode2.append(fn2.split('*')[0])
            else:
                fatherNode2.append(fn2)
        else:
            fatherNode2.append('')
    #一个父节点
    else:
        #以/作为分割
        if regex2.findall(bm):
            fatherNode1.append(re.sub(regex2,'.',bm).split('.')[0])
            fatherNode2.append('')
        else:
            fatherNode1.append(bm.split('.')[0])
            fatherNode2.append('')
# print(len(fatherNode1))
# print(len(fatherNode2))



# 创建excel文件
father = pd.DataFrame({'father1' : fatherNode1 , 'father2' : fatherNode2})
out = pd.ExcelWriter('father.xls')
father.to_excel(out)
out.save()
