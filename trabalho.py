from datetime import date
from datetime import datetime 

def preço(cp, cg):
    MCF =  (cp * 20 + cg * 40) * 20 / 100 + cp * 20 + cg * 40 #MEU canino feliz 2KM Final de semana + 20%

    MCFU = cp * 20 + cg * 40 #MEU canino feliz 2KM dia de semana cp = $20 cg= $40
 
    VR = cp * 20 + cg * 55 # final de semana

    VRU = cp * 15 + cg * 50 # Dia de semana 

    CHOW = cp * 30 + cg * 40 # todos os dias  cp = $30 e cg = $40
    return MCF,MCFU,VR,VRU,CHOW


def erro (msg):
  while True:
    try:
      z = float(input(msg))
    except (TypeError, ValueError):
      print('Erro de digitação, tente novamente')
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
  str_date = input(str('Quando será sua ida ao Petshop?\n\nOBS: CASO O VALOR NÃO SEJA DIGITADO CORRETAMENTE, O PROGRAMA FECHARA.\n\nAqui um modelo de data a ser inserido: XX/XX/2009\n'))
  date = datetime.strptime(str_date, '%d/%m/%Y').date()
  indice_da_semana = date.weekday()
  date = DIAS[indice_da_semana] #TRANSFORMANDO STR EM DIA DA SEMANA capiturando dados

  X = erro('Qual a quantidade de cachorros pequenos?\n')
  Y = erro('Qual a quantidade de cachorros grandes?\n')

  MCF, MCFU, VR, VRU, CHOW = preço(X, Y)

  M = ('Meu canino feliz')
  V = ('Vai Rex')
  C = ('ChowChowgas')

  if (date == 'Sábado'):
    if VR < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VR}')
    elif VR < CHOW:
      print (f'No dia {str_date} que será no {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VR}')
    elif CHOW < MCF:
      print (f'No dia {str_date} que será no {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
    elif CHOW < VR:
      print (f' No dia {str_date} que será no {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
  elif (date == 'Domingo'):
    if VR < MCF:
      print (f'No dia {str_date} que sera no {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VR}')
    elif VR < CHOW:
      print (f'No dia {str_date} que sera no {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VR}')
    elif CHOW < MCF:
      print (f'No dia {str_date} que sera no {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
    elif CHOW < VR:
      print (f' No dia {str_date} que sera no {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
  else:
    if MCFU < VRU:
      print (f'No dia {str_date} que sera na {date} o melhor preço será no Petshop {M}, o valor do banho é de R${MCFU}')
    elif VRU < MCFU:
      print (f'No dia {str_date} que sera na {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VRU}')
    elif VRU < CHOW:
      print (f'No dia {str_date} que sera na {date} o melhor preço será no Petshop {V}, o valor do banho é de R${VR}')
    elif CHOW < MCFU:
      print (f'No dia {str_date} que sera na {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
    elif MCFU < CHOW:
      print (f'No dia {str_date} que sera na {date} o melhor preço será no Petshop {M}, o valor do banho é de R${MCFU}')
    elif CHOW < VRU:
      print (f' No dia {str_date} que sera na {date} o melhor preço será no Petshop {C}, o valor do banho é de R${CHOW}')
    if MCFU == VRU:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais proximo.')
    elif VRU == CHOW:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {V}, pois está mais proximo.')
    elif MCFU == CHOW:
      print (f'Como os preços ficaram parecidos, a melhor escolha é o petshop {C}, pois está mais proximo.')
  break
print ('=-=' * 40)
print('Nos da GW Tecnologia agradecemos sua presença, até logo!')
print ('=-=' * 40)
print('Precione a tecla ENTER para fechar o programa.')
input()
