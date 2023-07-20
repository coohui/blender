# Alex落地
# hight = 100  # 原始高度
# distance = 0  # 记录经过的距离
#
# for i in range(10):
#     # 先将下落高度加入到总和中
#     distance += hight  # distance = distance + hight
#     if i == 9:
#         break
#     # 计算反弹高度
#     hight = hight / 2  # hight /= 2
#
#     # 再将反弹高度加入到总和中
#     distance += hight
#
# print(f"共经过了{distance}米")


# 九九乘法表
# 控制被乘数
# for i in range(1, 10):
# 控制乘数
# for j in range(1, i + 1):
#     print(f"{j}*{i}={j * i}", end="\t")
# print() #end = '\n\n'


# 年会抽奖
import random  # 随机数

staff_list = []
for user in range(1, 301):
    staff_list.append(f"员工{user}")

# winnerList3 = random.sample(staff_list, 30)
# print(winnerList3)
# winnerList2 = random.sample(staff_list, 6)
# print(winnerList2)
# winnerList1 = random.sample(staff_list, 3)
# print(winnerList1)
level = [30, 6, 3]
for i in range(3):
    winnerList = random.sample(staff_list, level[i])

    for winner in winnerList:
        staff_list.remove(winner)

    print(f"获得{3 - i}等奖的是：{winnerList}")
    print(f"还剩{len(staff_list)}个人未中奖")
