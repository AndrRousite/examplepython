# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
import time


def ex1():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print(i, j, k)


# ex1()


# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def ex2():
    num = int(input("请输入金额："))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if num > arr[idx]:
            r += (num - arr[idx]) * rat[idx]
            num = arr[idx]
    print("您的利润为： ", r)


# ex2()


# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：
#   假设该数为 x。
#   1、则：x + 100 = n2, x + 100 + 168 = m2
#   2、计算等式：m2 - n2 = (m + n)(m - n) = 168
#   3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
#   4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
#   5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
#   6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
#   7、接下来将 i 的所有数字循环计算即可。
def ex3():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n * n - 100
                print(x)


# ex3()

# 输入某年某月某日，判断这一天是这一年的第几天？
def ex4():
    year = int(input("year : "))
    month = int(input("month : "))
    day = int(input("day : "))
    count = day
    for i in range(1, month):
        if i in (1, 3, 5, 7, 8, 10, 12):
            count += 31
        elif i == 2:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                count += 29
            else:
                count += 28
        else:
            count += 30
    print("it is the %dth day.", count)


# ex4()

# 输入三个整数x,y,z，请把这三个数由小到大输出。
def ex5():
    ll = []
    for i in range(3):
        ll.append(input("请输入: "))
    ll.sort()
    print(ll)


# ex5()


# 斐波那契数列。
def ex6(num):
    a, b = 1, 0
    for i in range(num):
        print(b)
        a, b = b, a + b


# ex6(10)

# 将一个列表的数据复制到另一个列表中。
def ex7():
    arr1 = [1, "liu-feng", 'hehe']
    arr2 = arr1[:]
    print(arr2)


# ex7()

# 输出 9*9 乘法口诀表。
def ex8():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, " * ", i, " = ", i * j, "\t", end="")
        print()


# ex8()

# 暂停一秒输出。
def ex9():
    lll = ["hehe", "haha", "heiehie"]
    for i in range(lll.__len__()):
        print(lll[i])
        time.sleep(1)


ex9()

