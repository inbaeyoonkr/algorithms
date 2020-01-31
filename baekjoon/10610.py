import sys


def greedy(number):
    sum = 0
    if '0' not in number:
        return -1
    else:
        for i in number:
            sum += int(i)
        if(sum % 3 != 0):
            return -1
        else:
            return(''.join(number))


if __name__ == "__main__":
    number = list(sys.stdin.readline().strip())
    print(greedy(sorted(number, reverse=True)))


"""
* "".join(list) : 리스트에서 문자열으로

"""
