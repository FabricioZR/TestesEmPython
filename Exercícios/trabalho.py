import math
print("----TRABALHO DE PEDRO E FABRICIO----")
print('-----Ola seja(m) bem vindas(os)-----')
print('\nDigite 0 para Estimativa da Média de uma População')
print("ou")
print('Digite 1 para Estimativa da Proporção de uma População\n')
duv=int(input('0 ou 1: '))
if duv == 0:
    n = int(input('Digite o número de elementos da amostra (n): '))
    N = int(input('Digite o número de elementos da população(N): '))
    m = float(input('Digite o valor da média(m): '))
    s = float(input('Digite o valor do desvio padrão(s): '))
    gc = float(input('Digite o grau de confiança(%): '))
    if gc == 90: gc = 1.65
    elif gc == 95: gc = 1.96
    elif gc == 99: gc = 2.58
    vlm = m

    cor=n/N*100
    if cor < 5:
        x = math.sqrt(n)
        e = s/x
        ee = gc*e
        ep = m+ee
        en = m-ee
        erro = ee
        print('Média Pontual:',m)
        print('Média intervalar: %.2f'%en,'e','%.2f'%ep)
        print('Erro: %.2f'%ee)
    else :
        x = math.sqrt(n)
        e = s/x
        ee = gc*e
        cr = math.sqrt(N-n)
        crr = math.sqrt(N-1)
        crf = cr/crr
        ee = ee*crf
        ep = m+ee
        en = m-ee
        erro = ee
        print('Média pontual: ',m)
        print('Média intervalar: %.2f'%en,'a','%.2f'%ep)
        print('Erro: %.2f'%erro)
else:
    n = int(input('Digite o valor de n: '))
    N = int(input('Digite o valor de N: '))
    x = int(input('Digite o número de itens da amostra (x): '))
    gc = float(input('Digite o grau de confiança(%): '))
    pm = float(input('Digite o valor da proporção amostral(p), caso não seja informado, digite 0):'))
    if gc == 90: gc = 1.65
    elif gc == 95: gc = 1.96
    elif gc == 99: gc = 2.58
    cor=n/N*100
    if cor < 5:
        if pm == 0 :
                   pm = x/n
        pf = pm*100
        cs = pm*(1-pm)
        e = math.sqrt(cs)
        ee = math.sqrt(n)
        ei = e/ee
        eif = gc*ei
        ep = pm+eif
        en = pm-eif
        print('Estimativa Pontual: %.1f'%pf)
        print('Estimativa Intervalar: %.2f'%en,'a','%.2f'%ep)
        print('Erro: %.d%%'%(eif*100))
    else :
        if pm == 0 :
            pm = x/n
        pf = pm*100
        cs = pm*(1-pm)
        e = math.sqrt(cs)
        ee = math.sqrt(n)
        ei = e/ee
        cr = N-n
        crr = N-1
        r = math.sqrt(cr)
        rr = math.sqrt(crr)
        dr = r/rr
        eif = gc*ei*dr
        ep = pm+eif
        en = pm-eif
        print('Estimativa pontual: %.1f'%pf,'%')
        print('Estimativa intervalar: %.2f'%en,'a','%.2f'%ep)
        print('Erro: %.d%%'%(eif*100))
