def eh_par(a):
    if a % 2 == 0 or a == 0:
        return True
    return False


def analizar_paridade(lista):
    a = 0
    b = 0
    c = 0

    for i in lista:
        if i == '{':
            a += 1
        if i == '}':
            a += 1
        
        if i == '[':
            b += 1
        if i == ']':
            b += 1
        
        if i == '(':
            c += 1
        if i == ')':
            c += 1
    
    print(a, b, c)

    l = []
    if eh_par(a):
        l.append(True)
    if not eh_par(a):
        l.append(False)

    if eh_par(b):
        l.append(True)
    if not eh_par(b):
        l.append(False)

    if eh_par(c):
        l.append(True)
    if not eh_par(a):
        l.append(False)
    
    if all(l):
        return 'S'
    return 'N'

n = int(input())
expressoes = [list(input()) for _ in range(n)]

for i in expressoes:
    print(analizar_paridade(i))