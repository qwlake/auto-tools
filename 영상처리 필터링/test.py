a = [list(map(int, input().split())) for _ in range(10)]
f1 = [[1,1,1],[1,1,1],[1,1,1]]
f1_sum = 9
f2 = [[1,1,1],[1,5,1],[1,1,1]]
f2_sum = 18
f3 = [[1,1,1],[1,-8,1],[1,1,1]]
f3_sum = 9
f_list = [f1,f2,f3]
sum_list = [f1_sum,f2_sum, f3_sum]
d = [
    [-1,-1],[-1,0],[-1,1],
    [0,-1], [0,0], [0,1],
    [1,-1], [1,0], [1,1]]

def print_res(res):
    for i in range(10):
        print(res[i])
    print()

for f, s in zip(f_list, sum_list):
    res = []
    for i in range(10):
        t = []
        for j in range(10):
            sum = 0
            for k in range(9):
                sum += a[(i+d[k][0])%10][(j+d[k][1])%10]
            t.append(int(sum/s))
        res.append(t)
    print_res(res)