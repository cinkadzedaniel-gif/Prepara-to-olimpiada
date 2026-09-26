n = int(input())
a_list = list(map(int, input().split()))

count = 0

for i in range (1,n):

    if a_list[1] > a_list[i-1]:
        count += 1

print(count)