import re

# r 以只读方式打开文件。这是默认模式。文件必须存在，不存在抛出错误
#rb 以二进制格式打开一个文件用于只读。
#r+ 打开一个文件用于读写。文件指针将会放在文件的开头。读完就追加。
#w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
#  也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
#   文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

# Python中的相对路径是相对于运行的文件的路径的
# 开发程序对 stock_data.txt 进行以下操作：
f = open('F:\git\python\stock_data.txt', 'r', encoding='utf-8')

# f.read() # 读全部内容
# f.write('写操作')
headers = f.readline().strip().split(',')

stock_dic = {}
for line in f:
    line = line.strip()
    line = line.split(',')
    stock_dic[line[0]] = line

# 没关闭它，会一直占用系统资源
f.close() 

# 程序启动后，给用户提供查询接口，允许用户重复查股票行情信息。

while True:  # 死循环
    cmd = input('输入查询的指令：')

    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]

        # 允许用户通过模糊查询股票名，比如输入“啤酒”,
        # 就把所有名称当中包含啤酒的股票都打印出来。
        if cmd in s_name:
            print(s_data)

    # 允许按 当前价、涨跌幅、换手率这几列来筛选信息，
    # 比如输入“当前价>50”则把价格大于50的股票都打印，
    # 输入“涨跌幅<50“，则把涨跌幅小于50的股票都打印，不用判断等于。

    # 公式查询
    # 1. 判断公式的合法性（正则表达式）
    cmd_parser = re.split('[<>]', cmd)
    print(cmd_parser)
    if len(cmd_parser) != 2:
        print('输入的公式不合法，重新输入！')
        continue

    # 2. 判断列名的合法性
    filter_column, filter_val = cmd_parser
    if filter_column not in ['当前价', '涨跌幅', '换手率']:
        print('输入的列名不合法，重新输入！')
        continue

    # 3. 判断数值的合法性
    try:  # 尝试
        filter_val = float(filter_val)
    except:
        print('输入的数值不合法，重新输入！')
        continue

    # 4. 处理逻辑
    # 4.1 取索引    ------------   headers
    column_index = headers.index(filter_column)

    for s_id, s_data in stock_dic.items():
        if '>' in cmd:
            if float(s_data[column_index].strip('%')) > filter_val:
                print(s_data)
        else:
            if float(s_data[column_index].strip('%')) < filter_val:
                print(s_data)
