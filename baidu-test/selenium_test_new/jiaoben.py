#一天能充5次币，一天最多可以充300个币

# 请输入您充值的金额：
# 1.第充一次币，一次充xx元,当前还可充值四次币,还可充值余额xx元
# 2.第充两次币，两次充xx元,当前还可充值三次币，还可充值余额xx元
# 3.第充三次币，三次充xx元,当前还可充值二次币,还可充值余额xx元
# 4.第充四次币，四次充xx元,当前还可充值一次币，还可充值余额xx元
# 5.第充五次币，五次充xx元,当前充值次数已用完！
# 6.再次充入会报错，提示您已超过当天充值次数范围！
#在每次充值的金额中做判断，充值的金额累计大于300会报错，提示已超过当天充值金额

# n = 0 # 次数
# sumMoney = 0
# while n < 5:
#     while sumMoney <= 300:
#         money = int(input("请输入金额: "))
#         if money <= 300:
#             sumMoney += money
#             if sumMoney <= 300:
#                 n += 1
#                 print("您第{}次充值{}元,还可充值{}次,充值余额{}".format
#                       (n,money,5-n,sumMoney))
#             else:
#                 print("您最多还能充值{}元".format(300-sumMoney+money))
#         else:
#             print("您最多输入{}！".format(300-sumMoney))
#             print("对不起,您已超出当天充值的范围！")
#     else:
#         break


a = [1,2,3,4,5,6]
b = ["a","b","c","d","e","f"]
# db = [str(x) +str(y) for x,y in zip(b,a)]
# print(db)
print([x*y for  x,y in zip(b,a)])

a = "awfesdafhjkcasadckjsdackjsadvcnksausafdsch"
b = "SufhwrifjiEIJFDIEJDIej"
list1 = list(a+b)
list2 = sorted(list1)
print(''.join(list2))