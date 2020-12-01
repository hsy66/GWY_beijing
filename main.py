import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
from prettytable import MSWORD_FRIENDLY, PLAIN_COLUMNS
import prettytable

gettime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
p = open("C://Users//Administrator//Desktop//result.txt", "w")
api = "https://sc.ftqq.com/SCU96918Tb2c5be23a8317a33d67c9f43efb4631d5eb434b78030c.send"
table = PrettyTable(["职位代码", "报考单位", "报考职位", "招考人数", "面试比例", "已报人数", "报考比例"])
#table.set_style(MSWORD_FRIENDLY)
table.align["报考单位"] = 'l'
table.align["报考职位"] = 'l'
table.align["报考比例"] = 'l'


#a = [820729002, 231141902, 231167205, 231549402, 220116801, 220161202]
a = [241668601,232501301,232501401,232501501,232501502,232501601,232501701,232501702,232501801,232502001,232502301,242502601,823306501,230521606,230627603,830625703,220161202,220116801,820729002,231141902,231167205,231549402]
arr1 = []
arr2 = []
for i in a:
    url = "http://fuwu.rsj.beijing.gov.cn/gwyquery/publicQuery/gzwbkrsssquery"
    data = {
        "zwdm": i
    }
    res = requests.post(url=url, data=data)
    soup = BeautifulSoup(res.content, 'lxml')

    tr = soup.find_all('tr')[2]

    td1 = tr.find_all('td')[0:7]

    a = str(td1)
    aa = a.replace('</td>', '').replace('<td>', '').replace(' ', '').replace('[', '').replace(']', '').replace('艰苦边远地区派出所、检查站等一线职位', '艰苦地区')

    list1 = aa.strip(',').split(',')
    arr1.append(aa)

    table.add_row(list1)
print(table)

print(table, file=p)
print(gettime, file=p)

p.close()
