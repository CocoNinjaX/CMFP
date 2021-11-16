import math 
print('~~Dev CocoNinja~~')
print()
print(f'📌│Olá seja bem vindo(a) ao painel de \nconfiguração da CMFP,\no que vamos calcular hoje?\n\n1.Operações Simples(adição, subtração,\ndivisão, multiplicação).\n\n2.Equação de Segundo Grau(bhaskara)\n\n3.Função de primeiro grau.\n\n4.Função de segundo grau.\n\nAlguma dúvida sobre a calculadora?Então use:\n\n5.Para ver respostas sobre dúvidas gerais.\n\n📌│Digite o número do modo que você deseja usar:\n ')
modo = input()
print('')
if modo == '1':
  print('📳│Iniciando modo 1:')
  print('')
  x = int(input('📝│Qual o primeiro número? '))
  print('')
  y = int(input('📝│Qual o segundo número? '))
  adição = (x+y)
  subtração = (x-y)
  multiplicação = (x*y)
  divisão = (x/y)
  print('')
  print(f'✅│Suas respostas:\n\nAdição: {x} + {y} = {adição}\n\nSubtração: {x} - {y} = {subtração}\n\nDivisão: {x} / {y} = {divisão}\n\nMultiplicação: {x} x {y} = {multiplicação} ')
if modo == '2':   
 a = int(input('📝│Na sua equação qual o valor de A? '))
 print('')
 b = int(input('📝│Na sua equação qual o valor de B? '))
 print('')
 c = int(input('📝│Na sua equação qual o valor de C? '))
 print('')
 primeiro = int(b*-1)
 delta2 = int(-4*a*c)
 delta3 = int(b**2 -4*a*c)
 delta1 = int(b**2)
 if delta3 >= 0:
   raiz1 = math.sqrt(delta3)
   raiz2 = int(delta3**(1/2))
   raiz = (raiz1-raiz2)
   divisor = int(2*a)
   soma = int(primeiro+raiz2)
   subtração = int(primeiro-raiz2)
   x1 = (soma/divisor)
   x2 = (subtração/divisor)
   if delta2 >= 0:
     if raiz == 0:
       print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} + {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nx = {primeiro} ± {raiz2}\n       {divisor}\n\nx1 = {primeiro} + {raiz2}\n       {divisor}\n\nx1 = {soma}\n     {divisor}\n\nx1 = {x1}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X1)\n\nx2 = {primeiro} - {raiz2}\n       {divisor}\n\nx2 = {subtração}\n     {divisor}\n\nx2 = {x2}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X2)')
     else:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\nSua equação não possí raiz exata... (√{delta3} = {raiz1}')
   else:
      if raiz == 0:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nx = {primeiro} ± {raiz2}\n       {divisor}\n\nx1 = {primeiro} + {raiz2}\n       {divisor}\n\nx1 = {soma}\n     {divisor}\n\nx1 = {x1}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X1)\n\nx2 = {primeiro} - {raiz2}\n       {divisor}\n\nx2 = {subtração}\n     {divisor}\n\nx2 = {x2}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X2)')
      else:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\nSua equação não possí raiz exata... (√{delta3} = {raiz1}')
 else:
    print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nSua equação não possui solução por ter delta negativo ({delta3})')
if modo == '3':
  print('📳│Iniciando modo 3:')
  print('')
  a = int(input('📝│Na sua equação qual o valor do primeiro número? '))
  b = int(input('📝│Na sua equação qual o valor do segundo número? '))
  if a == 1:
    psl = (b*-1)
    print(f'✅│Zero: Y = X {b}\n\n {psl} = X\n\nZero: X = {psl}')
  if 0 >= b:
    if a >= b:
      psl = (b*-1)
      div = (a/psl)
      print(f'✅│Zero: Y = {a}X {b}\n\n {psl} = {a}X\n\nX = {a}\n     {psl}\n\n✅│Resultado da divisão: {div}')
    else:
      psl = (a*-1)
      div = (b/psl)
      print(f'✅│Zero: Y = {a}X {b}\n\n {psl} = {b}X\n\nX = {b}\n     {psl}\n\n✅│Resultado da divisão: {div}')
  if a != 1:
    if a >= b:
      psl = (b*-1)
      div = (a/psl)
      print(f'✅│Zero: Y = {a}X {b}\n\n {psl} = {a}X\n\nX = {a}\n     {psl}\n\n✅│Resultado da divisão: {div}')
    else:
      psl = (a*-1)
      div = (b/psl)
      print(f'✅│Zero: Y = {a}X {b}\n\n {psl} = {b}X\n\nX = {b}\n     {psl}\n\n✅│Resultado da divisão: {div}')
  print('')
  print('📋│Tabela:')
  n5 = ((a*-5)+b)
  n4 = ((a*-4)+b)
  n3 = ((a*-3)+b)
  n2 = ((a*-2)+b)
  n1 = ((a*-1)+b)
  n0 = ((a*0)+b)
  p1 = ((a*1)+b)
  p2 = ((a*2)+b)
  p3 = ((a*3)+b)
  p4 = ((a*4)+b)
  p5 = ((a*5)+b)
  if b >= 0:
    print(f'X  / {a}X + {b} / Y\n-5 /{a}.(-5)+{b} / {n5} (-5,{n5})\n-4 /{a}.(-4)+{b} / {n4}  (-4,{n4})\n-3 /{a}.(-3)+{b} / {n3}  (-3,{n3})\n-2 /{a}.(-2)+{b} / {n2}  (-2,{n2})\n-1 /{a}.(-1)+{b} / {n1}  (1,{n1})\n 0 /{a} .0 +{b} / {n0}  (0,{n0})\n 1 /{a} .1 +{b} / {p1}  (1,{p1})\n 2 /{a} .2+ {b} / {p2}  (2,{p2})\n 3 /{a} .3 +{b} / {p3}  (3,{p3})\n 4 /{a} .4 +{b} / {p4}  (4,{p4})\n 5 /{a} .5 +{b} / {p5}  (5,{p5})')
  else:
        print(f'X  / {a}X  {b} / Y\n-5 /{a}.(-5){b} / {n5}  (-5,{n5})\n-4 /{a}.(-4) {b} / {n4}  (-4,{n4})\n-3 /{a} .(-3) {b} / {n3}  (-3,{n3})\n-2 /{a}.(-2) {b} / {n2}  (-2,{n2})\n-1 /{a}.(-1) {b} / {n1}  (-1,{n1})\n 0 /{a} .0 {b} / {n0}  (0,{n0})\n 1 /{a} .1 {b} / {p1}  (1,{p1})\n 2 /{a} .2 {b} / {p2}  (2,{p2})\n 3 /{a} .3 {b} / {p3}  (3,{p3})\n 4 /{a} .4 +{b} / {p4}  (4,{p4})\n 5 /{a} .5 {b} / {p5}  (5,{p5})')
if modo == '4':   
 a = int(input('📝│Na sua equação qual o valor de A? '))
 print('')
 b = int(input('📝│Na sua equação qual o valor de B? '))
 print('')
 c = int(input('📝│Na sua equação qual o valor de C? '))
 print('')
 primeiro = int(b*-1)
 delta2 = int(-4*a*c)
 delta3 = int(b**2 -4*a*c)
 delta1 = int(b**2)
 if delta3 >= 0:
   raiz1 = math.sqrt(delta3)
   raiz2 = int(delta3**(1/2))
   raiz = (raiz1-raiz2)
   divisor = int(2*a)
   soma = int(primeiro+raiz2)
   subtração = int(primeiro-raiz2)
   x1 = (soma/divisor)
   x2 = (subtração/divisor)
   if delta2 >= 0:
     if raiz == 0:
       print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} + {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nx = {primeiro} ± {raiz2}\n       {divisor}\n\nx1 = {primeiro} + {raiz2}\n       {divisor}\n\nx1 = {soma}\n     {divisor}\n\nx1 = {x1}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X1)\n\nx2 = {primeiro} - {raiz2}\n       {divisor}\n\nx2 = {subtração}\n     {divisor}\n\nx2 = {x2}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X2)')
     else:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\nSua equação não possí raiz exata... (√{delta3} = {raiz1}')
   else:
      if raiz == 0:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nx = {primeiro} ± {raiz2}\n       {divisor}\n\nx1 = {primeiro} + {raiz2}\n       {divisor}\n\nx1 = {soma}\n     {divisor}\n\nx1 = {x1}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X1)\n\nx2 = {primeiro} - {raiz2}\n       {divisor}\n\nx2 = {subtração}\n     {divisor}\n\nx2 = {x2}\n(Caso a divisão não de exata(1.0,2.0,...) simplefique o X2)')
      else:
        print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta1} {delta2}\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\nSua equação não possí raiz exata... (√{delta3} = {raiz1}')
 else:
    print(f'✅│Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nSua equação não possui solução por ter delta negativo ({delta3})')
 primeiro = int(b*-1)
 delta2 = int(-4*a*c)
 delta3 = int(b**2 -4*a*c)
 delta1 = int(b**2)
 if delta3 >= 0:
   raiz1 = math.sqrt(delta3)
   raiz2 = int(delta3**(1/2))
   raiz = (raiz1-raiz2)
   if raiz == 0:
     print(f'✅│Zero: X1 {x1}, X2 {x2}')
 xv = int(((b*-1)/(2*a)))
 yv = int(((delta3*-1)/(4*a)))
 print(f'VERTICE X: -b = -({b}) = {b*-1} = {xv}\n           2.a    2.{a}  {2*a} \nVERTICE Y: -Δ = -({delta3})= {delta3*-1} =  {yv}\n           4.a    4.{a}  {4*a}')
 print('')
 print('📋│Tabela:')
 n5e = ((-5)**2)
 n5a = (a*n5e)
 n5b = (b*-5)
 n5 = (n5a+n5b+c)
 n4e = ((-4)**2)
 n4a = (a*n4e)
 n4b = (b*-4)
 n4 = (n4a+n4b+c)
 n3e = ((-3)**2)
 n3a = (a*n3e)
 n3b = (b*-3)
 n3 = (n3a+n3b+c)
 n2e = ((-2)**2)
 n2a = (a*n2e)
 n2b = (b*-2)
 n2 = (n2a+n2b+c)
 n1e = ((-1)**2)
 n1a = (a*n1e)
 n1b = (b*-1)
 n1 = (n1a+n1b+c)
 n0e = ((0)**2)
 n0a = (a*n0e)
 n0b = (b*0)
 n0 = (n0a+n0b+c)  
 p1e = ((1)**2)
 p1a = (a*p1e)
 p1b = (b*1)
 p1 = (p1a+p1b+c) 
 p2e = ((2)**2)
 p2a = (a*p2e)
 p2b = (b*2)
 p2 = (p2a+p2b+c)
 p3e = ((3)**2)
 p3a = (a*p3e)
 p3b = (b*3)
 p3 = (p3a+p3b+c)
 p4e = ((4)**2)
 p4a = (a*p4e)
 p4b = (b*4)
 p4 = (p4a+p4b+c)
 p5e = ((5)**2)
 p5a = (a*p5e)
 p5b = (b*5)
 p5 = (p5a+p5b+c)
 if b >= 0:
   if c >= 0:
     print(f'X  / {a}X²+{b}X+{c} / Y\n-5 / {a}.(-5)²+{b}.(-5)+{c} / {n5}  (-5,{n5})\n-4 / {a}.(-4)²+{b}.(-4)+{c} / {n4}  (-4,{n4})\n-3 / {a}.(-3)²+{b}.(-3)+{c} / {n3}  (-3,{n3})\n-2 / {a}.(-2)²+{b}.(-2)+{c} / {n2}  (-2,{n2})\n-1 / {a}.(-1)²+{b}.(-1)+{c} / {n1}  (-1,{n1})\n 0 / {a}.(0)²+{b}.0+{c} / {n0}  (0,{n0})\n 1 / {a}.(1)²+{b}.(1)+{c} / {p1}  (1,{p1})\n 2  / {a}.(2)²+{b}.(2)+{c} / {p2}  (2,{p2})\n 3 / {a}.(3)²+{b}.(3)+{c} / {p3}  (3,{p3})\n 4 / {a}.(4)²+{b}.(4)+{c} / {p4}  (4,{p4})\n 5 / {a}.(5)²+{b}.(5)+{c} / {p5}  (5,{p5})')
   else:
     print(f'X  / {a}X²+{b}X {c} / Y\n-5  / {a}.(-5)²+{b}.(-5){c} / {n5}  (-5,{n5})\n-4 / {a}.(-4)²+{b}.(-4){c} / {n4} (-4,{n4})\n-3 / {a}.(-3)²+{b}.(-3){c} / {n3} (-3,{n3})\n-2 / {a}.(-2)²+{b}.(-2){c} / {n2} (-2,{n2})\n-1 / {a}.(-1)²+{b}.(-1){c} / {n1} (-1,{n1})\n 0 / {a}.(0)²+{b}.0{c} / {n0} (0,{n0})\n 1 / {a}.(1)²+{b}.(1){c} / {p1} (1,{p1})\n 2 / {a}.(2)²+{b}.(2){c} / {p2} (2,{p2})\n 3 / {a}.(3)²+{b}.(3){c} / {p3} (3,{p3})\n 4 / {a}.(4)²+{b}.(4){c} / {p4} (4,{p4})\n 5 / {a}.(5)²+{b}.(5){c} / {p5} (5,{p5})')
 else:
   if c >= 0:
     print(f'X  / {a}X²{b}X+{c} / Y\n-5 / {a}.(-5)²{b}.(-5)+{c} / {n5} (-5,{n5})\n-4 / {a}.(-4)²{b}.(-4)+{c} / {n4} (-4,{n4})\n-3 / {a}.(-3)²{b}.(-3)+{c} / {n3} (-3,{n3})\n-2 / {a}.(-2)²{b}.(-2) + {c} / {n2} (-2,{n2})\n-1 / {a}.(-1)²{b}.(-1)+{c} / {n1} (-1,{n1})\n 0 / {a}.(0)²{b}.0+{c} / {n0} (0,{n0})\n 1 / {a}.(1)²{b}.(1)+{c} / {p1} (1,{p1})\n 2 / {a}.(2)²{b}.(2)+{c} / {p2} (2,{p2})\n 3 / {a}.(3)²{b}.(3)+{c} / {p3} (3,{p3})\n 4 / {a}.(4)²{b}.(4)+{c} / {p4} (4,{p4})\n 5 / {a}.(5)²{b}.(5)+{c} / {p5} (5,{p5})')
   else:
     print(f'X  / {a}X²{b}X {c} / Y\n-5 / {a}.(-5)²{b}.(-5){c} / {n5} (-5,{n5})\n-4 / {a}.(-4)²{b}.(-4){c} / {n4} (-4,{n4})\n-3 / {a}.(-3)²{b}.(-3){c} / {n3} (-3,{n3})\n-2 / {a}.(-2)²{b}.(-2){c} / {n2} (-2,{n2})\n-1 / {a}.(-1)²{b}.(-1){c} / {n1} (-1,{n1})\n 0 / {a}.(0)²{b}.0{c} / {n0} (0,{n0})\n 1 / {a}.(1)²{b}.(1){c} / {p1} (1,{p1})\n 2 / {a}.(2)²{b}.(2){c} / {p2} (2,{p2})\n 3 / {a}.(3)² {b}.(3)  {c} / {p3} (3,{p3})\n 4 / {a}.(4)²{b}.(4){c} / {p4} (4,{p4})\n 5 / {a}.(5)²{b}.(5){c} / {p5} (5,{p5})')
 if 0 > delta3:
   print(f'🅱️ │Calculando Bhaskara:\n\nx = – b ± √Δ\n       2a\n\n∆ = b² -4.a.c\n\n∆ = ({b})² -4.({a}).({c})\n\n∆ = {delta3}\n\nx = – ({b}) ± √{delta3}\n       2.{a}\n\nSua equação não possui solução por ter delta negativo ({delta3})')    