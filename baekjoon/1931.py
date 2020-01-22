import sys


def greedy(time_table):
    meeting_count = 0
    start_time = 0
    for time in time_table:
        if time[0] >= start_time:
            start_time = time[1]
            meeting_count += 1
    return meeting_count


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    time_table = []
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().strip().split())
        time_table.append((start, end))

    # 시작 시간을 기준으로 정렬
    time_table = sorted(time_table, key=lambda time: time[0])
    # 종료 시간을 기준으로 정렬
    time_table = sorted(time_table, key=lambda time: time[1])

    print(greedy(time_table))
