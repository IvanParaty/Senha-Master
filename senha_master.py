from random import randint
def testar_resposta(esc, cores, core):
    res = -1
    for v in range(len(esc)):
#        print(esc,len(esc),v)
        cc = int(esc[v])
#        print(cc)
        co = cores[cc - 1]
        print(f'{core[co]}-{ co }-', end='')
        if co in lista and int(v) == lista.index(co):
            res = 2
            resp.append(res)
        elif co in lista and int(v) != lista.index(co):
            res = 1
            resp.append(res)
        else:
            res = 0
            resp.append(res)
    resp.sort()

###    Inicio
resp = []
lista = []
cont = 0
cores = ('Branco', 'Amarelo', 'Vermelho', 'Verde', 'Azul', 'Roxo')
core = {'limpa':'\033[m]',
        'Branco':'\033[m',
        'Amarelo':'\033[33m',
        'Vermelho':'\033[31m',
        'Verde':'\033[36m',
        'Azul':'\033[34m',
        'Roxo':'\033[35m'}
print(core['Azul'])
while cont != 4:
    num = int(randint(1, 6))
    if cores[num - 1] in lista != True:
        ex =+ 1
    else:
        lista.append(cores[num - 1])
        cont = cont + 1

print ('Olá, vamos jogar. Sortei quatro cores das relacionadas abaixo, sem repetir.'
       ' \nVoce deve descobrir quais as cores que sorteie e suas posições.'
       '\nescolha quatro numeros de cores; para cada: \ncor e posição certa ==> 2 \nsó a cor certa =======> 1  \ncor errada ===========> 0')
print('\033[m1 - Branco \033[:33m2 - Amarelo \033[:31m3 - Vermelho \033[:36m4 - Verde \033[:34m5 - Azul \033[:35m6 - Roxo\033[m\n', '-=' * 30)

cont = 0
tst = []
while cont != 10 :
    esc = str(input('Escolha quatro cores ==> '))
    esc = esc.strip()
 #   esc = esc.split()
    testar_resposta(esc, cores, core)
    cont = cont + 1
    print(f'\033[m  {resp}')
    soma = 0
    for d in range(len(resp)):
        soma += resp[d]
        if soma == 8:
            print(f'Parabens, voce venceu em {cont} jogadas')
            quit()
    resp.clear()


print('A sequncia que escolhi foi  ==>  ', end='')
for v in range(len(lista)):
    cc = lista[v]
    print(f'{core[cc]}-{ cc }-', end='')

print ('\033[m')
print()
print ('Fim do teste')
