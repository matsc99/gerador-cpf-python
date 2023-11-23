import random

# Define os nove primeiros digitos do cpf
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Define primeiro digito validador
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Define segundo digito validador
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Valida o cpf gerado com o cpf enviado pelo usuário
cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado)
