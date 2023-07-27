import os, sys

# ret = os.access('F:\git\python\stock_data.txt', os.F_OK)
# print ("F_OK- 测试path是否存在 - 返回值 %s"% ret)

# ret = os.access('F:\git\python\stock_data.txt', os.R_OK)
# print ("R_OK- 读 - 返回值 %s"% ret)

# ret = os.access('F:\git\python\stock_data.txt', os.W_OK)
# print ("W_OK- 写 - 返回值 %s"% ret)

# ret = os.access('F:\git\python\stock_data.txt', os.X_OK)
# print ("X_OK- 是否可执行 - 返回值 %s"% ret)

# os.chdir() 方法用于改变当前工作目录到指定的路径
# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)

# 修改当前工作目录
# os.chdir('F:/redis')

# 返回当前工作目录
# retval = os.getcwd()
# print ("当前工作目录为 %s" % retval)

# 重命名文件或目录
# os.replace('F:\git\python\data.txt', 'F:\git\python\data.txt')

# 当前工作目录
# path = os.getcwd()
# print("当前工作目录: ", path)
# 父目录
# parent = os.path.join(path, os.pardir)
# 父目录
# print("\n父目录:", os.path.abspath(parent))

# 列出目录
print ("目录为: %s"%os.listdir(os.getcwd()))

# 删除路径
os.rmdir() # 传参目录名字

# 列出重命名后的目录
print ("目录为: %s" %os.listdir(os.getcwd()))

# os.remove("aa.txt")

