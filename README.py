peso = float(input())
altura = float(input())

imc = peso/altura**2

if imc<=18.5:
  print ('Abaixo do peso')
else:
  if imc>18.5 and imc<=24.9:
    print('Normal' )  
  else:
    if imc>24.9 and imc<=29.9:
      print('Excesso de peso')
    else:
      if imc>29.9 and imc<=34.9:
        print('Obsidade Leve (Grau I)')
      else:
        if imc>34.9 and imc<=39.9:
          print('Obsidade Severa (Grau II)')
        else:
          if imc>39.9:
            print('Obsidade Mórbida (Grau III)')
            
          

  
