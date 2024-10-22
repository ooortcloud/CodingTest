def check(src, dst):
    global graph

    searchList = []
    searchList.append(src)
    
    # 중복 탐색 방지를 위한 방문 리스트 작성
    visitList = []

    while searchList:
        next = searchList.pop()
        visitList.append(next)
        for nodeList in graph[next]:
            for index, val in enumerate(nodeList):
                if (val == 1) and (index not in visitList):
                    if index == dst:
                        return 1
                    else:
                        searchList.append(index)            

    return 0

n = int(input())

graph = [[]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(check(i, j), end=" ")
    print()