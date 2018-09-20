#剪绳子问题，给定长度为n的绳子，将绳子剪成m段，m段长度相乘最大值
#问题有两种解法，一种是动态规划，还有一种是贪婪算法（有一定的数学证明）。
#动态规划
def maxProduct(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    products = [0,1,2,3]
    for i in range(4,n+1):
        max = 0
        for j in range(1,i//2+1):
            df = products[j]*products[i-j]
            if max < df:
                max = df
        products.append(max)
    return products[n]
print(maxProduct(8)) #18


#贪婪算法
def maxProductSolution(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    count_3 = n//3
    if n%3 == 1:
        return 3**(count_3-1)*4
    else:
        return 3**count_3*(n%3 if n%3 != 0 else 1)
print(maxProductSolution(9))


