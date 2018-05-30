#while 循环
# count = 0
# while count <= 50:
#     print("loop",count)
#     count += 1

#打印0-100的偶数
# count = 0
# while count <= 100:
#     if count % 2 ==0:
#         print("loop",count)
#     count += 1

#在1-100内不打印50 并打印60-80的平方
# count = 0
# while count <= 100:
#     if count ==50:
#         pass #就是直接过不输出
#     elif count >= 60 and count <= 80:
#             print(count * count)
#     else:
#         print("loop", count)
#     count += 1

#死循环 While
# count = 0
# while True:#True本身就为真 条件就一直被满足
#     print("kobe",count)
#     count +=1

#循环的终止语句
# break语句
# count = 0
# while count <= 100:
#     print("loop",count)
#     if count == 5:
#         break
#     count += 1

#continue语句
# count = 0
# # while count <= 100:
# #     print("loop",count)
# #     if count == 5:
# #         continue# 跳出本次循环 继续下一次循环
# #     count += 1

count = 0
while count <= 100:
    count += 1
    if count >5 and count<95 :
        continue
    print("loop", count)

