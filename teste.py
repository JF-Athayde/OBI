import matplotlib.pyplot as plt

# Cada linha: x1, y1, x2, y2 (canto sup. esquerdo e canto inf. direito)
retangulos = [list(map(int, input().split())) for _ in range(int(input()))]

fig, ax = plt.subplots()

for x1, y1, x2, y2 in retangulos:
    largura = x2 - x1
    altura = y1 - y2
    ax.add_patch(plt.Rectangle((x1, y2), largura, altura,
                               fill=False, edgecolor='blue'))

    # Marcar cantos
    ax.plot([x1, x2], [y1, y2], 'ro')  # apenas para destacar

ax.set_aspect('equal')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Retângulos a partir dos cantos")
plt.grid(True)
plt.show()
