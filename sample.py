def backTracking(row):

    global cnt, n, queenExistList

    if row == n:
        cnt += 1
        return

    for col in range(n):

        queenExistList[row] = col
        if checkQueen(row):
            backTracking(row+1)

def checkQueen(currentRow):

    global queenExistList

    for row in range(currentRow):
        if queenExistList[row] == queenExistList[currentRow]:
            return False
        
        if abs(currentRow - row) == abs(queenExistList[currentRow] - queenExistList[row]):
            return False
        
    return True

n = int(input())

queenExistList = [0] * n

cnt = 0
backTracking(0)
print(cnt)