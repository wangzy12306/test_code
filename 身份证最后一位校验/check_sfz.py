#coding=utf-8
import re
#"41111119901610000x"
#"412721199311191115"

class sfzl :
    def __init__(self,num):
        if None == re.match(r'(^[0-9]{17}[0-9xX]$)',num) :
            print("身份证输入错误 {}".format(num))
            return
        self.num = num
        self.jishuan()
    def mi(self,cishu):
        t = 1
        for i in range(1, 19 - cishu):
            t = t * 2
        t = t % 11
        return t
    def jishuan(self):
        jy = 0
        #计算身份证与权重的乘积结果
        for i in range(17):
            jy += self.mi(i + 1) * int(self.num[i])
        #计算乘积结果除11的余数
        jy %= 11
        #计算余数对应的最后一位
        zh = str((12 - jy) % 11)
        # 如果余数为10改为X
        if zh == '10':
            zh = 'x'
        #判断最后一位是否正确
        if self.num[17] == zh:
            print("正确身份证 {}".format(self.num))
        else:
            print("错误身份证 {} 最后一位是{}".format(self.num, zh))

ll = sfzl("41111119901610000x")


