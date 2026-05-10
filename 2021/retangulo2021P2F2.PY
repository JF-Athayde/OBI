def prefix_Sum(vector):
    result = [0]
    pot = 0
    for v in vector:
        pot += v
        result.append(pot)
    
    return result

def binary_search(array, target, n):
    left = 0
    right = len(array)-1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle

        elif array[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1

def main(vector, n):
    ps = prefix_Sum(vector)
    diam = ps[-1]/2
    diam_cont = 0

    for i in range(n):
        r = binary_search(ps, diam+ps[i], n)
        if r != -1:
            diam_cont += 1
        
        if diam_cont == 2:
            return 'S'
    
    return 'N'

vector = [3, 3, 4, 2, 6, 2, 2, 2]
n = 8

print(main(vector, n))
