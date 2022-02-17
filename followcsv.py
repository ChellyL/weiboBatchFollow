# 处理从 药方 导出的关注列表csv文件
import csv

follow = csv.reader(open('following-1376755973-20220215.csv', encoding="utf-8"))
data = list(follow)

# 获取关注者的 userid 的列表
def getlist():
    link = []
    for i in data:
        if i[1][0] == "#":
            # print(i)
            pass
        else:
            link.append(i[2])
    link.remove(link[0])
    clean_link = []
    for m in link:
        n = int(m[20:])
        # n = m[20:]
        clean_link.append(n)
    return clean_link

# 获取关注者的 昵称和userid 的字典
def getdict():
    people = {}
    for i in data:
        people[i[1]] = i[2]
    del people['name']
    return people
