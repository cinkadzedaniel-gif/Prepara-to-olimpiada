n, x = map(int, input().split())

y_list = list(map(int, input().split()))

result = []

for y in y_list:
    lower = (x // y) * y
    upper = lower + y 

    if (x - lower ) <= (upper - x):
        x = lower

    else:
        x = upper


    result.append(x)

print(*result)
