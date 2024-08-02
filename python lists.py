if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command, *rest = input().split()
        for i in range(len(rest)):
            rest[i] = int(rest[i])
        if command == "insert":
            list.insert(rest[0], rest[1])
        elif command == "print":
            print(list)
        elif command == "remove":
            list.remove(rest[0])
        elif command == "append":
            list.append(rest[0])
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop(-1)
        elif command == "reverse":
            list.reverse()
