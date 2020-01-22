import sys


def greedy(rope):
    value = []
    for i in range(len(rope)):
        value.append(rope[i] * (i+1))
    return max(value)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    rope = []
    for _ in range(n):
        rope.append(int(sys.stdin.readline().strip()))
    rope.sort(reverse=True)
    print(greedy(rope))
