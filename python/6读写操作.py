from sys import path
# print(path)
f = open('F:\git\python\data.txt', 'r+', encoding='utf-8')
# print(f.read()) #从文件读取指定的字节数，如果未给定或为负则读取所有
# print(f.readlines()) #读取所有行并返回列表	
# 将字符串写入文件，返回的是写入的字符长度
f.write('我是写入的')
# 移动文件读取指针到指定位置
# 可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；
# 0 代表从文件开头开始算起，
# 1 代表从当前位置开始算起，
# 2 代表从文件末尾算起
f.seek(0, 2) #从第二个位置开始偏移一位
f.write('我是追加的')
# 返回文件当前位置
# print(f.tell())
# 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
# 截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小
# f.truncate()
# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符
# f.writelines('test')
f.seek(0, 0) #从第二个位置开始偏移一位
print(f.read())