n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜 알고리즘 활용
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (graph[i][k] + graph[k][j] == 2):
                graph[i][j] = 1

for i in range(n):
    print(' '.join(map(str, graph[i])))