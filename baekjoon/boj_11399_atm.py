import sys
sys.stdin = open('input.txt')
N = int(input())
people = list(map(int, input().split()))
people.sort()
total_time = [0]*N
total_time[0] = people[0]
for i in range(1, N):
    total_time[i] = total_time[i-1]+people[i]
print(sum(total_time))