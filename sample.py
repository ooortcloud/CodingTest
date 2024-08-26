n, k = map(int, input("n, k").split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

# A는 오름차순 정렬.
# B는 내림차순 정렬.
listA.sort()
listB.sort(reverse=True)

for i in range(k):
    listA[i], listB[i] = listB[i], listA[i]

sum = 0
for num in listA:
    sum += int(num)

print(sum)