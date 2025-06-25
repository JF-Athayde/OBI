caixa = [int(input()) for _ in range(3)]
caixa.sort()

caixa = [caixa[0], caixa[1]]
janela = [int(input()) for _ in range(2)]

if janela[0] >= caixa[0] and janela[1] >= caixa[1]:
    print('S')
elif janela[1] >= caixa[0] and janela[0] >= caixa[1]:
    print('S')
else:
    print('N')