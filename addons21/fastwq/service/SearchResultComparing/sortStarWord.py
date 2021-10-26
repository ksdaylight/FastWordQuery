# -*- coding:utf-8 -*-




import random

def dictionairy():
    # 声明字典
    googleNaram2w = {}

    i = 1
    with open('../../../../../dict/project/ankiexport/GNFinal.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            googleNaram2w[line] =i
            i += 1
   #  key: 1  value: example
   # 声明字典
    outPut = {}
    with open('../../../../../dict/project/ankiexport/klin3final.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            temp = googleNaram2w.get(line, 0)
            if temp == 0:
                temp = random.randint(0,1000)
            outPut[line]= temp
    # key:example value: 在上个词典中能找到的序号，或随机数
    # # 初始化
    # key_value[2] = 56
    # key_value[1] = 2
    # key_value[5] = 12
    # key_value[4] = 24
    # key_value[6] = 18
    # key_value[3] = 323

    # print("按键(key)排序:")

    # # sorted(key_value) 返回重新排序的列表
    # # 字典按键排序
    # for i in sorted(googleNaram2w):
    #     print((i, googleNaram2w[i]), end=" ")
    print("按值(value)排序:")
    outF = sorted(outPut.items(), key=lambda kv: (kv[1], kv[0]))
    print(outF)


    f = open('../../../../../dict/project/ankiexport/outputKlin3.txt', 'a')
    i = 0
    for t in outF:
        f.write('\n'+t[0])
        # print('\n'+t[0])
        i += 1
    f.close()

def main():
    # 调用函数
    dictionairy()


# 主函数
if __name__ == "__main__":
    main()