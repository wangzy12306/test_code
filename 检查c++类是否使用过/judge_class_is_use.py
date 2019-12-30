#coding=utf-8
import os,re
file_list = {}
regex = re.compile("class\s+(.*?)\s*:")  #匹配类名的正则表达式
def get_file(path = os.getcwd()):
    list = os.listdir(path)
    for l in list:
        if os.path.isdir(path + '\\' + l) and l[0] != '.':
            get_file(path + '\\' + l)
        elif l[0] != '.' and os.path.splitext(l)[-1] in ['.cpp','.hpp','.c','.h']:
            with open(path + '\\' + l) as f:
                txt = f.readlines()
                if len(txt) != 0:
                    file_list[path + '\\' + l] = ''.join(txt)
                    print 'write ' + path + '\\' + l + ' to Memory!'

def judge_use():
    for key in file_list.keys():                    #遍历文件看
        for cls in regex.findall(file_list[key]):   #查找文件中存在的类名
            is_use = 0
            for key2 in file_list.keys():           #查找此类是否出现在其它文件中
                if key2 == key:
                    continue
                if cls in file_list[key2]:          #出现过一次就不在寻找,查找其他类名
                    is_use = 1
                    break;
            if is_use == 0:                         #一次没出现旧打印出文件名+类名
                print key + ' calss ' + cls + ' : is not use in other files'

if __name__ == '__main__':
    get_file()
    judge_use()