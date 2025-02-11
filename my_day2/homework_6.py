# 2024年12月25日
a = input('输入一个整数')
sum = 0
i = 1
# if(int(a)<0):
#     a = ~int(a) + 1
while(i<=63):
    # print(a)
    if(int(a)%2!=0):
        sum =sum +1

    a = int(a)>>1
    i+=1
print(sum)




