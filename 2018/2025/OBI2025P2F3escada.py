def mostrar(lista):
    for a in lista:
        print(a, end=' ')

def resolver_intervalado(escada_intervalada):
    a = 0
    b = len(escada_intervalada)-1

    escada_ = escada_intervalada[a:b+1]

    for i_, _ in enumerate(escada_[1:-1]):
        i = i_ + 1

        new = escada_[i-1] + 1

        dist = b-i
        dif = abs(escada_[b]-new)

        if dif > dist:
            new_dif = abs(escada_[b]-new)-1
            new_dist = b-i


            if new_dif > new_dist:
                new -= 1

            new -= 1
        
        escada_[i] = new

    return escada_

def matrizar(escada):
    escada_ = escada[::-1]
    escada_.append(0)
    escada_ = escada_[::-1]
    escada_.append(0)
    
    intervalos = [i for i, deg in enumerate(escada_) if deg != -1]
    matriz = [escada_[intervalos[i]:intervalos[i+1]+1] for i in range(len(intervalos)-1)]

    matriz[0] = matriz[0][1:]
    matriz[-1] = matriz[-1][:-1]

    return matriz

def completar(a_):
    a = a_

    def c(a):
        ma = max(a)
        for i in range(len(a)):
            a[i] = ma + i

        return a

    if a[0] == -1:
        return c(a[::-1])[::-1]

    else:
        return c(a)

def resolver(escada):
    escada_matriz = matrizar(escada)

    i0 = escada_matriz[0]
    if i0[0] != -1 and i0[-1] != -1:
        mostrar(resolver_intervalado(i0))
    else:
        mostrar(completar(i0))

    for intervalo in escada_matriz[1:]:
        if intervalo[0] != -1 and intervalo[-1] != -1:
            mostrar(resolver_intervalado(intervalo)[1:])
        else:
            mostrar(completar(intervalo)[1:])
    print()

input()
escada = list(map(int, input().split()))
resolver(escada)