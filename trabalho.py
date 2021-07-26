from time import sleep
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
print ('Seja bem vindo!')
print ('=-=' * 40)
sleep (1)
nome = str(input('Digite seu nome: '))
print ('=-=' * 40)
print(f'Sr(a) {nome}, é um prazer receber você por aqui!\nNós somos a GW tecnologia e queremos sempre lhe ajudar, usando o maximo de praticidade e comodidade possível.\nHoje iremos analizar o melhor custo-benéficio para dar banhos em seus amados PETs.\nPara isso, selecionamos alguns PetsShops e precisamos de algumas informaçoes.')
print ('=-=' * 40)
print ('=-=' * 40)

while True:
  DIAS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
  str_date = input(str('Quando será sua ida ao Petshop?\n\nAqui um modelo de data a ser inserido: 00/00/2009\n'))
  try:
    date = datetime.strptime(str_date, '%d/%m/%Y').date()
  except ValueError:
    print('!' * 42)
    print('MODELO DE DATA INCORRETO, TENTE NOVAMENTE.')
    continue
  else:
    indice_da_semana = date.weekday()
    date = DIAS[indice_da_semana] #TRANSFORMANDO STR EM DIA DA SEMANA capiturando dados

  print('\nOs cachorros de porte pequeno são aqueles que podem chegar a medir até 40 cm – sendo esse tamanho calculado desde as patas até os ombros do cão. O peso da maioria desses pets chega a ser de 10 kg.\nJá cães considerados grandes, medem até 70 cm e pesam de 25 até 45 kg.\n')
  
  X = erro('Qual a quantidade de cachorros porte pequenos?\n')
  Y = erro('Qual a quantidade de cachorros porte grandes?\n')
  
  MCF, MCFU, VR, VRU, CHOW = preço(X, Y) #Atribui a função 'preço' nas variaveis X e Y

  M = ('Meu canino feliz')
  V = ('Vai Rex')
  C = ('ChowChowgas')
  print ('=-=' * 40)
  print ('carregando informações:')
  sleep(1)
  print('.')
  sleep(.5)
  print('.')
  sleep(.5)
  print('.')
  sleep(.5)
  print('\n' * 20)
  print ('=-=' * 40)
  if (date == 'Sábado'):
    if VR < MCF:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {V}, o valor total do banho é de R${VR}\n')
    elif VR < CHOW:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {V}, o valor total do banho é de R${VR}\n')
    elif CHOW < MCF:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {C}, o valor total do banho é de R${CHOW}\n')
    elif CHOW < VR:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {C}, o valor total do banho é de R${CHOW}\n')
  elif (date == 'Domingo'):
    if VR < MCF:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {V}, o valor total do banho é de R${VR}\n')
    elif VR < CHOW:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {V}, o valor total do banho é de R${VR}\n')
    elif CHOW < MCF:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {C}, o valor total do banho é de R${CHOW}\n')
    elif CHOW < VR:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {C}, o valor total do banho é de R${CHOW}\n')
  else:
    if MCFU < CHOW:
      print (f'\nNo dia {str_date}, {date}, o melhor preço é no Petshop {M}, o valor total do banho é de R${MCFU}\n')
    if MCFU == VRU:
      print (f'\nComo os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais próximo.\n')
    if VRU == CHOW:
      print (f'\nComo os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais próximo.\n')
    if MCFU == CHOW:
      print (f'\nComo os preços ficaram parecidos, a melhor escolha é o petshop {C}, pois está mais próximo.\n')
  break
print ('=-=' * 40)
print('\nNos da GW Tecnologia agradecemos sua presença, até logo!\n')
print ('=-=' * 40)
print('Desenvolvido por: Otávio Valadão  tel:(31) 9 9886-6134\nGmail: otavionunesvaladao@gmail.com')
print ('=-=' * 40)
print('\nPrecione a tecla ENTER para fechar o programa.')

print('\n' * 3)
input()
