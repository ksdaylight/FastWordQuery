# -*- coding:utf-8 -*-




import random

def dictionairy():
    # 声明字典
    haveLearnedFinal = {}

    i = 1
    with open('../../../../../dict/project/ankiexport/haveLearnedFinal.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            haveLearnedFinal[line] =i
            i += 1

   # 声明字典
    outPut = {}
    with open('../../../../../dict/project/ankiexport/outputKlin4.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            temp = haveLearnedFinal.get(line, 0)
            outPut[line]= temp


    # print("按值(value)排序:")
    outF = outPut.items()
    # outF = sorted(outPut.items(), key=lambda kv: (kv[1], kv[0]))
    print(outF)


    # f = open('../../../../../dict/project/ankiexport/outputKlin4Sign.txt', 'a')
    # i = 0
    # for t in outF:
    #     f.write('\n'+t[0])
    #     # print('\n'+t[0])
    #     i += 1
    # f.close()

def main():
    # 调用函数
    dictionairy()


# 主函数
if __name__ == "__main__":
    main()