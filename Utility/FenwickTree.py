class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.bit = [0] * (self.n + 1)

    # Atualiza o índice i (1-based) adicionando valor 'val'
    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    # Retorna a soma dos elementos de 1 até i (1-based)
    def prefix_sum(self, i):
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= i & -i
        return result

    # Retorna a soma do intervalo [l, r] (1-based)
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)


# Exemplo de uso:

# inicializa Fenwick Tree para vetor de tamanho n
n = 10
ft = FenwickTree(n)

# adicionar valores iniciais (supondo array original 'a' 1-based)
a = [0, 3, 2, 1, 5, 4, 6, 7, 8, 9, 10]  # a[0] ignorado
for i in range(1, n+1):
    ft.update(i, a[i])

# soma do intervalo [2, 5]
print(ft.range_sum(2, 5))  # Exemplo: 2+1+5+4 = 12

# atualiza posição 3 adicionando +4
ft.update(3, 4)

# soma novamente
print(ft.range_sum(2, 5))  # Agora 2+(1+4)+5+4 = 16
