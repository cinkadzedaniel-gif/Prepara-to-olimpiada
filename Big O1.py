n = int(input())
a_list = list(map(int, input().split()))

god_list = list(set(a_list))
great_list = sorted(god_list)

print(great_list[-2])
   