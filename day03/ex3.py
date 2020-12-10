f = open("input.txt", "r")

matrice = []

for riga in f:
    riga = riga.replace("\n", "")
    matrice.append(riga)

def count_tree(matrice, down, right):
    numbers_of_tree = 0
    current_index = right
    for i in range(down, len(matrice), down):
        if matrice[i][current_index % 31] == "#":
            numbers_of_tree += 1
        current_index += right
    return numbers_of_tree


down_right = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

val = 1
for coppia in down_right:
    val *= count_tree(matrice, coppia[0], coppia[1])

print(val)