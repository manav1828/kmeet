
X = []
O = []

winning = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

while len(X) + len(O) < 9:

    a = int(input("X: Which box? "))
    if a in X or a in O or a < 1 or a > 9:
        print("Invalid or already occupied box!")
        continue
    X.append(a)

    if any(set(c).issubset(set(X)) for c in winning):
        print("X wins!")
        break

    if len(X) + len(O) == 9:
        break

    b = int(input("O: Which box? "))
    if b in X or b in O or b < 1 or b > 9:
        print("Invalid or already occupied box!")
        continue
    O.append(b)

    if any(set(c).issubset(set(O)) for c in winning):
        print("O wins!")
        break

if len(X) + len(O) == 9:
    if not any(set(c).issubset(set(X)) for c in winning) and not any(set(c).issubset(set(O)) for c in winning):
        print("It's a draw!")

print("X positions:", X)
print("O positions:", O)

     























    