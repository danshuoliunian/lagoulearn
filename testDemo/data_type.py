# 冒泡排序

numbs = [3, 6, 5, 44, 76, 86, 75, 35, 45, 88]

for i in range(len(numbs) - 1):
    for j in range(len(numbs) - 1 - i):
        if numbs[j] < numbs[j + 1]:
            numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]
        print("第" + str(j) + "次内循环" + str(numbs))
    print("第" + str(i) + "次外循环" + str(numbs))
print("最后的结果" + str(numbs))
