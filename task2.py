N = int(input("Введите количество кустов: "))
berries = []
for j in range(N):
    berry = int(input(f"Введите количество ягод на кусте {j+1}: "))
    berries.append(berry)

max_berries = 0

for i in range(N):
    if i == 0:
        total = berries[i] + berries[N-1] + berries[(i+1) % N]
    elif i == N-1:
        total = berries[i] + berries[i-1] + berries[(i+1) % N]
    else:
        total = berries[i] + berries[i-1] + berries[i+1]

    if total > max_berries:
        max_berries = total

print("Максимальное количество собранных ягод:", max_berries)
