import sys


def greedy(p):
    p.sort()
    waiting_time = 0
    total_time = 0
    for time in p:
        waiting_time += time
        total_time += waiting_time
    return total_time


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().strip().split()))
    print(greedy(p))
