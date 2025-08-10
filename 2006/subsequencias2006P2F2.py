from itertools import combinations

def gerar_subsequencias(seq, n):
    return list(set(''.join(a) for a in combinations(seq, n)))

def contar(s1, s2):
    c1 = {a:0 for a in list(set(s1))}    
    c2 = {a:0 for a in list(set(s2))}    

    for s in s1:
        c1[s] += 1
    
    for s in s2:
        c2[s] += 1
    
    i = 1
    while True:
        sub_s1 = gerar_subsequencias(s1, i)

        for sub in sub_s1:
            c3 = {a:0 for a in list(set(sub))}
            for c in sub:
                c3[c] += 1
            
            for c in sub:
                if c2[c] < c3[c]:
                    return i
        i += 1

s1, s2 = 'ababaa', 'abbaa'
print(contar(s1, s2))

