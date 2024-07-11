quantidade_linhas = int(input())

for j in range (1, (quantidade_linhas*4)+1):
    if j%4 == 0:
        print("PUM")
    else:
        print(f"{j}", end=" ") 