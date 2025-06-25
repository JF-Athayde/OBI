def pode_dividir(N, x1, y1, x2, y2):
    meio = N // 2
    if (x1 < meio and x2 >= meio) or (x2 < meio and x1 >= meio):
        print("S")
        return
    if (y1 < meio and y2 >= meio) or (y2 < meio and y1 >= meio):
        print("S")
        return
    print("N")

N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

pode_dividir(N, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
