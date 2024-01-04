#fórmula do imc: kg / m^2(altura)

#colocar variáveis de peso e altura
peso = float(input("qual o peso? "))
altura = float(input("qual a altura? "))

#fazer o cálculo
imc = peso / altura**2

# separar por obesidade
if imc < 18.5:
    print('magreza extrema')
elif imc >= 18.5 and imc <= 24.99:
    print('peso ideal')
elif imc >= 25 and imc <= 29.99:
    print('soprepeso')
elif imc >= 30 and imc <= 34.99:
    print('obesiade I')
elif imc >= 35 and imc <= 39.99:
    print('obesidade II')
elif imc > 40:
    print('obesidade III')
else:
    print('inexistênte')

print("seu imc é ", imc)