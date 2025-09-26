def contar(seq):
    seq_un = list(set(seq))
    dict_cont = {a:0 for a in seq_un}

    for s in seq:
        dict_cont[s] += 1
    
    return dict_cont

def condicao_existencia(contagem):
    if max(contagem.values()) > 4:
        return 'N'
    return 'S'

bolas = list(map(int, input().split()))  # list(map(int, input().split()))
seq = contar(bolas)
print(condicao_existencia(seq))