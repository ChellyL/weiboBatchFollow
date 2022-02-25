# 将已经获取的关注list处理为每30个id为一组的列表

def getgroup():
    list = []
    all = len(list)
    total = all / 30
    if type(total) != "int":
        total = int(all / 30) + 1

    start = 0
    end = 30

    group30 = []
    for i in range(total):
        group = list[start:end]
        group30.append(group)
        # print(group)
        start += 30
        end += 30

    return bgroup30
