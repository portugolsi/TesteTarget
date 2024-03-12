
# Função que calcula a sequência de Fibonacci
def fibonacci(n):
    fibonacci = [0, 1] # Crio uma lista com os dois primeiros valores da sequência
    while fibonacci[-1] < n: # Enquanto o valor do último indície for menor que o valor que eu digitei
        proximo_fibonacci = fibonacci[-1] + fibonacci[-2] # Calculo o próximo valor
        fibonacci.append(proximo_fibonacci) # adiciono ao final da lista
    return fibonacci

# Função que verifica se o número perte ou não à sequência de Fibonnaci
def verifica_pertence(n, fibonacci):
    if n in fibonacci: # verifico se o valor que digitei pertence ou não à lista
        return f"{n} pertence a sequência de Fibonacci."
    else:
        return f"{n} não pertence a sequência de Fibonacci."



n = int(input())

seq_fibonacci = fibonacci(n)
print(verifica_pertence(n,seq_fibonacci))