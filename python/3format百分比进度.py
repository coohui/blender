name = "张三"
age = 18
address = "北京市"
sex = "男"
float_num = 123.12345

# 当{}中存在数字时，数字对应变量的索引，会按照数字取format函数中的值进行填充。需要注意，索引的值是从0开始。{}中的数字，不能超过变量的索引，否则会报错。
print("姓名：{1} \n年龄：{2} \n地址：{0} \n".format(name, age, address))
# 也可以用key值直接指定
print('{name}网址： {site}'.format(name='我推', site='www.5tweb.com'))

import time

# {}或者{:}则代表输出的是字符串
# {:d}、{:06d} 代表输出的是十进制数值，接收的数字是int类型的。如果变量是其他类型的，会报错
for i in range(101):
  print("\r{}%".format(i),end=' ')
  time.sleep(0.05)

