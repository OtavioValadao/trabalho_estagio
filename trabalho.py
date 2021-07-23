from datetime import date
from datetime import datetime 

def preço(cp, cg):
    MCF =  (cp * 20 + cg * 40) * 20 / 100 + cp * 20 + cg * 40 #MEU canino feliz 2KM Final de semana + 20%

    MCFU = cp * 20 + cg * 40 #MEU canino feliz 2KM dia de semana cp = $20 cg = $40
 
    VR = cp * 20 + cg * 55 # final de semana

    VRU = cp * 15 + cg * 50 # Dia de semana 

    CHOW = cp * 30 + cg * 40 # todos os dias  cp = $30 e cg = $40
    return MCF,MCFU,VR,VRU,CHOW

def erro (msg):
  while True:
    try:
      z = int(input(msg))
    except (TypeError, ValueError):
      print('Valor incorreto, tente novamente.')
      continue
    else:
      return z


print ('=-=' * 40)
print ('Olá tudo bem?')
nome = str(input('Qual seu nome? '))
print ('=-=' * 40)
print(f'Sr(a) {nome}, é um prazer receber você por aqui!\nNos somos a GW tecnologia e queremos sempre lhe ajudar, usando o maximo de praticidade e comodidade possível.\nHoje iremos analizar o melhor custo-benéficio para dar banhos em seus amados PETs.\nPara isso, selecionamos alguns PetsShops e precisamos de algumas informaçoes.')
print ('=-=' * 40)
print ('=-=' * 40)

while True:
  DIAS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
  str_date = input(str('Quando será sua ida ao Petshop?\n\nAqui um modelo de data a ser inserido: XX/XX/2009\n'))
  try:
    date = datetime.strptime(str_date, '%d/%m/%Y').date()
  except ValueError:
    print('!' * 42)
    print('MODELO DE DATA INCORRETO, TENTE NOVAMENTE.')
    continue
  else:
    indice_da_semana = date.weekday()
    date = DIAS[indice_da_semana] #TRANSFORMANDO STR EM DIA DA SEMANA capiturando dados

  X = erro('Qual a quantidade de cachorros pequenos?\n')
  Y = erro('Qual a quantidade de cachorros grandes?\n')


  MCF, MCFU, VR, VRU, CHOW = preço(X, Y)

  M = ('Meu canino feliz')
  V = ('Vai Rex')
  C = ('ChowChowgas')

  print (MCF, VR, CHOW)

  if (date == 'Sábado'):
    if VR < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {V}, o valor do banho é de R${VR}')
    elif VR < CHOW:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {V}, o valor do banho é de R${VR}')
    elif CHOW < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {C}, o valor do banho é de R${CHOW}')
    elif CHOW < VR:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {C}, o valor do banho é de R${CHOW}')
  elif (date == 'Domingo'):
    if VR < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {V}, o valor do banho é de R${VR}')
    elif VR < CHOW:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {V}, o valor do banho é de R${VR}')
    elif CHOW < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {C}, o valor do banho é de R${CHOW}')
    elif CHOW < VR:
      print (f'No dia {str_date} que será no {date} o melhor preço é no Petshop {C}, o valor do banho é de R${CHOW}')
  else:
    if MCFU < CHOW:
      print (f'No dia {str_date} que será na {date} o melhor preço é no Petshop {M}, o valor do banho é de R${MCFU}')
    if MCFU == VRU:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais próximo.')
    if VRU == CHOW:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais próximo.')
    if MCFU == CHOW:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {C}, pois está mais próximo.')
  break
print ('=-=' * 40)
print('Nos da GW Tecnologia agradecemos sua presença, até logo!')
print ('=-=' * 40)
print('Precione a tecla ENTER para fechar o programa.')
input()
