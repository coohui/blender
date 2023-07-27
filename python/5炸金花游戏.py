# 《炸金花》底层逻辑实现
#
# 自己写一个程序，实现发牌、比大小判断输赢。
#
# 游戏规则：
# 一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢。
#
# 有以下几种牌：
#       豹子：三张一样的牌，如3张6.
#       同花顺：即3张同样花色的顺子， 如红桃 5、6、7
#       顺子：又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子
#       对子：2张牌一样
#       单张：单张最大的是A
#   这几种牌的大小顺序为， 豹子>同花顺>同花>顺子>对子>单张


# 需程序实现的点：
# 先生成一付完整的扑克牌
# 给5个玩家随机发牌


# 统一开牌，比大小，输出赢家是谁
# 1. 单牌之间如何比较大小(权重)
# 2. 不同牌型之间如何比较大小
# A：红桃J  红桃K    黑桃A     1.1 + 13 + 140 = 154.1

# B：方片2  方片2    梅花3     0.2 + 2  +  30 =  32.2  * 5  = 161

# 3. 如何判断玩家手里是个什么牌（不同的牌型之间要有不同的判断方法）  高内聚  低耦合


# val = [2, 3, 3]   #--->   {2,3}
# if len(set(val)) == 2:
#     print("这就是个对子")
# if len(set(val)) == 1:
#     print("这就是个豹子")


# 代码实现
import random


# 1. 生成牌
def alex():
    poke_types = ['♥', '♠', '♦', '♣']
    poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    poke_list = []
    for p_type in poke_types:
        count = 2
        for p_num in poke_nums:
            card = [f"{p_type}{p_num}", count]
            count += 1
            poke_list.append(card)
    # print(poke_list)
    return poke_list


pokeList = alex()

player = ['老元', '花钱乐', '午后狂睡', 'L.', '拾忆', '威亮']


# 2. 发牌
def blackGirl(pl, pk, pn):
    player_dic = {}
    for p_name in pl:
        p_cards = random.sample(pk, pn)

        for card in p_cards:
            pk.remove(card)

        player_dic[p_name] = p_cards
        print(f"为玩家【{p_name}】生成了一副牌:{p_cards}")
    return player_dic


playerDic = blackGirl(player, pokeList, 3)


# 3. 写每种牌型的判断函数
# 冒泡排序

def sortList(dataList):
    length = len(dataList)
    for i in range(length):
        for j in range(length - i - 1):
            if dataList[j][1] > dataList[j + 1][1]:
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
    return dataList


# 单张
def calculate_single(p_cards, score):
    # 初始化的分
    # score = 0
    p_cards = sortList(p_cards)
    weight_val = [0.1, 1, 10]
    count = 0
    for card in p_cards:
        score += card[1] * weight_val[count]
        count += 1
    print(f"计算单牌的结果是:{score}")
    return score


# 对子
def calculate_pair(p_cards, score):
    p_cards = sortList(p_cards)
    card_val = [i[1] for i in p_cards]
    if len(set(card_val)) == 2:
        if card_val[0] == card_val[1]:  # aab
            score = (card_val[0] + card_val[1]) * 50 + card_val[2]
        else:  # abb
            score = (card_val[1] + card_val[2]) * 50 + card_val[0]

    print(f"计算对子的结果是:{score}")
    return score


# 顺子
def calculate_straight(p_cards, score):
    p_cards = sortList(p_cards)
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if b - a == 1 and c - b == 1:
        score *= 100
    print(f"计算顺子的结果是:{score}")
    return score


# 同花
def calculate_same_color(p_cards, score):
    color_val = [i[0][0] for i in p_cards]
    if len(set(color_val)) == 1:
        score *= 1000
    print(f"计算同花的结果是:{score}")
    return score


# 同花顺
def calculate_same_color_straight(p_cards, score):
    # 先判断同花
    color_val = [i[0][0] for i in p_cards]
    if len(set(color_val)) == 1:
        # 再判断顺子
        p_cards = sortList(p_cards)
        card_val = [i[1] for i in p_cards]
        a, b, c = card_val
        if b - a == 1 and c - b == 1:
            score *= 0.1
    print(f"计算同花顺的结果是:{score}")
    return score


# 豹子
def calculate_leoard(p_cards, score):
    card_val = {i[1] for i in p_cards}
    if len(card_val) == 1:
        score *= 100000
    print(f"计算豹子的结果是:{score}")
    return score


# 4. 比对
calc_func_orders = [
    calculate_single,
    calculate_pair,
    calculate_straight,
    calculate_same_color,
    calculate_same_color_straight,
    calculate_leoard
]
playerScore = []
for p_name, p_cards in playerDic.items():
    print(f"开始计算玩家【{p_name}】的牌：{p_cards}")
    # 初始化得分
    score = 0

    for calc_func in calc_func_orders:
        score = calc_func(p_cards, score)
    playerScore.append([p_name, score])

winner = sortList(playerScore)[-1]

print(f"恭喜最后获胜的是：【{winner[0]}】，他的得分是：{winner[1]}")
