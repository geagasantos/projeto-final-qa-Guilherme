# Calculadora Simples em Python
def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida!"

# Testes básicos
assert calculadora(2, 3, '+') == 5, "Falha na soma"
assert calculadora(5, 2, '-') == 3, "Falha na subtração"
assert calculadora(4, 3, '*') == 12, "Falha na multiplicação"
assert calculadora(10, 2, '/') == 5, "Falha na divisão"
assert calculadora(5, 0, '/') == "Erro: Divisão por zero!", "Falha no tratamento de divisão por zero"

print("✅ Todos os testes passaram!")
