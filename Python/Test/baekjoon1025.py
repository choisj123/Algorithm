import sys

# 백준 2578

# 1. 빙고판 입력 받기
arr = []
for _ in range(5):
    arr.append(sys.stdin.readline().split())

# 2. 사회자가 부르는 수 list 담기
num = []
for _ in range(5):
    list = sys.stdin.readline().split()

    for i in list:
        num.append(i)

# 3. 빙고판 초기화
check_board = [[False for _ in range(5)] for _ in range(5)]

# 4. 빙고 수를 체크할 수 있는 함수
def check_row_bingo():
    count = 0
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if not check_board[i][j]:
                is_bingo = False
                break
        if is_bingo:
            count += 1
    return count

# 5. 빙고 column 수를 확인하기 위한 함수 구현
def check_column_bingo():
    count = 0
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if not check_board[j][i]:
                is_bingo = False
                break
        if is_bingo:
            count += 1
    return count

# 6. 대각선 빙고 수 확인하기 위한 함수 구현
def check_diagonal_bingo():
    count = 0
    # \ 모양 대각선
    is_bingo = True
    for i in range(5):
        if not check_board[i][i]:
            is_bingo = False
            break
    if is_bingo:
        count += 1
    
    # / 모양 대각선
    is_bingo = True
    for i in range(5):
        if not check_board[i][4 - i]:
            is_bingo = False
            break
    if is_bingo:
        count += 1

    return count


# 7. 사회자가 부르는 각 수에 대해 빙고판을 True로 체크하고,
#    만족하는 빙고의 수를 확인
for i in range(25):
    now_num = num[i]

    # 사회자가 부른 숫자의 빙고판 위치 확인하고 True로 표기
    for x in range(5):
        for y in range(5):
            if arr[x][y] == now_num:
                check_board[x][y] = True

    # 빙고판 True로 체크한 이후 빙고 몇개 완성됐는지 확인
    count = check_row_bingo() + check_column_bingo() + check_diagonal_bingo()

    # 완성된 빙고의 개수가 3개 이상이라면 해당 순서 출력
    if count >= 3:
        print(i + 1)
        break