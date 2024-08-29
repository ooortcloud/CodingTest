import sys

n, m = map(int, input().split())

riceCakeHeightList = list(map(int, sys.stdin.readline().split()))
# riceCakeHeightList.sort(reverse=True) # 이진탐색을 위해 내림차순 정렬


startHeight = min(riceCakeHeightList)
endHeight = max(riceCakeHeightList)
result = -1  # 조건을 만족하는 떡 길이
while startHeight <= endHeight:

    midHeight = (startHeight + endHeight) // 2

    total = 0  # 남는 떡의 최종 길이    
    # 전체 떡들에 대해서 커팅식
    for selectedHeight in riceCakeHeightList:
        if(midHeight < selectedHeight):
            total += (selectedHeight - midHeight)

    # 필요 이상으로 남는 떡의 길이가 긴 경우, 자르는 떡의 길이가 지금보다 긴 쪽으로 탐색 진행
    if total >= m:
        startHeight = midHeight + 1
        result = midHeight
    # 남는 떡의 길이가 부족한 경우, 자르는 떡의 길이가 지금보다 짧은 쪽으로 탐색 진행
    else:
        endHeight = midHeight - 1

print(result)