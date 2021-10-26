# -*- coding:utf-8 -*-




import random

import sys
import re

def mdxTxt():
   fsource = open('E:/dict/project/LDOCE6++ En-Cn V3-0.txt',"r+", encoding='utf-8')
   foutoutPut = open('E:/dict/project/LDOCE6++ En-Cn V3-0Replace.txt',"r+", encoding='utf-8')
   str1 = r'ldoce6ec.css'
   str2 = r'ldoce6ecReplace.css'
   for ss in fsource.readlines():
       tt = re.sub(str1,str2,ss)
       foutoutPut.write(tt)
   fsource.close()
   foutoutPut.close()

def main():
    # 调用函数
    mdxTxt()


# 主函数
if __name__ == "__main__":
    main()