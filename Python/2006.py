T = int(input())
linha = input().split()

count = 0

for i in range(5):
    if int(linha[i]) == T:
        count += 1
        
print(count)