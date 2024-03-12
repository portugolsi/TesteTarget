# 5) Escreva um programa que inverta os caracteres de um string.

string = input()

stringInvertida = ''

for i in range(len(string) - 1, -1, -1):
        
        stringInvertida += string[i]

print("String Invertida",stringInvertida)