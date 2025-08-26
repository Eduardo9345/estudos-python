num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritméticos

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 # Resto da divisão
exp = num1 ** num2 # Exponenciação

print(20 * "=")
print(sum)
print(sub)
print(div)
print(mult)
print(mod)
print(exp)

# Comparação

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2

bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"O número {num1} é igual ao número {num2}? {equal}")
print(f"O número {num1} é diferente do número {num2}? {different}")
print(f"O número {num1} é maior que o número {num2}? {bigger}")
print(f"O número {num1} é menor que o número {num2}? {smaller}")
print(f"O número {num1} é maior ou igual ao número {num2}? {bigger_equal}")
print(f"O número {num1} é menor ou igual ao número {num2}? {smaller_equal}")

# Atribuição

num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1