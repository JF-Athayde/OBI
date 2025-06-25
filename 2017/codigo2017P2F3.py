def igualdade(lista):
    return len(set(lista)) != len(lista)

def main(S):
    for a in S:
        for b in S:
            if a != b:
                for s in S:
                    if s in ''.join(a+b) and s != a and s != b:
                        return s
    return 'ok'

n = int(input())
S = [input() for _ in range(n)]

if igualdade(S):
    print(S[0])
else:
    print(main(S))