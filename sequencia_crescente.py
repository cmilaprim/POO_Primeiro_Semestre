while True:
    num = int(input())
    if num == 0:
        break
    else:
        for i in range(1, num + 1):
            print(i, end="")
            if i != num:
                print(' ', end='')
        print()