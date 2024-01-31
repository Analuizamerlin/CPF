import re

def cadastro_cpf():
    global cpf
    while True:
        cpf = input('CPF (xxx.xxx.xxx-xx): ')
            
        if not re.match(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}',cpf):
            print('Entrada inválida. Tente novamente!')
        else:
            break

def digito_verf(digitos, i):
   resto, soma = [0, 0], [0, 0]
   index = 8

   if i == 0:
    for mult in range (2,11):
      soma[i] = soma[i] + digitos[index] * mult
      index -= 1        
   else:
    soma[i] = dig_v[0] * 2
    for mult in range (3,12):
      soma[i] = soma[i] + digitos[index] * mult
      index -= 1
    
   resto[i] = soma[i] % 11

   if resto[i] <= 1:
      dig_v.append(0)
   else:
      dig_v.append(11 - resto[i])   

def valido(digitos):
   if (dig_v[0] == digitos[9]) and (dig_v[1] == digitos[10]):
      return True
   else:
      return False
    
global dig_v
dig_v, digitos = [], []

cadastro_cpf()

for num in cpf:
  if num.isdigit():
   digitos.append(int(num))

digito_verf(digitos, 0)
digito_verf(digitos, 1)
print(valido(digitos))