a = int(input())               #输入a
n = int(input())               #输入需要几个数相加
x = (((10**(n+1)-10)/9)-n)/9   #从1+11+111+...+11111...1的求和公式
print('计算和s =',a*x)