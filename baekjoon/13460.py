from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()
answer = 987654321


def init():
    _rx, _ry, _bx, _by = [0]*4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                _rx, _ry = i, j
            elif board[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True


def move(_x, _y, _dx, _dy, _c):
    while board[_x + _dx][_y + _dy] != '#' and board[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c


def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(d + 1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)


init()
bfs()


"""
* strip() : string을 " " 사이에 공백을 제거해서 준다. ex) string = "   xo " -> "xo"
* python에서 _(underscore)을 사용하는 경우
    1. 인터프리터의 last expression의 마지막 value를 저장할 때
    2. 특정 값을 신경쓰지 않을 때
    3. variables와 functions에 특별한 의미나 함수를 부여할 때
* collections.deque : front와 rear 양 쪽에서 추가와 제거가 가능한 자료구조
    - 왼쪽부터 오른쪽으로 초기화 한다.
    - append(x): 오른쪽 사이드에 추가
    - appendleft(x): 왼쪽 사이드에 추가. O(n)의 추가 소요
    - clear(): deque 안의 모든 element들을 제거하고 길이를 0으로 만듬
    - copy(): deque의 얕은 복사를 한다.
    - count(x): x와 동일한 element의 개수를 반환
    - pop(): 가장 우측에 있는 element를 제거하고 반환
    - popleft(): 가장 왼쪽에 있는 element를 제거하고 반환
    - remove(x): x를 찾아 제거한다.

"""
