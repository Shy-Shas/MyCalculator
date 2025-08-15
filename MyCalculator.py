def escolha_de_calculadora():

    def calculadora_normal():
        return eval(input('digite a operação: ')) #analisa a equação e já entrega o resultado

    def matriz():
        print('Calculadora de matriz 3x3')
        #linhas da matriz
        l1 = []
        l2 = []
        l3 = []
        #insere os números em cada linha
        for n in range(3):
            l1.append(float(input(f'digite o valor de a1,{n+1}: ')))
        for n in range(3):
            l2.append(float(input(f'digite o valor de a2,{n+1}: ')))
        for n in range(3):
            l3.append(float(input(f'digite o valor de a3,{n+1}: ')))

        #calcula a diagonal principal
        d_prim = ((l1[0] * l2[1] * l3[2]) + (l1[1] * l2[2] * l3[0]) + (l1[2] * l2[0] * l3[1]))
        #calcula a diagonal secundária
        d_sec = ((l1[2] * l2[1] * l3[0]) + (l1[0] * l2[2] * l3[1]) + (l1[1] * l2[0] * l3[2]))

        return (d_prim - d_sec) #retorna o determinante

    def trigonometria():
        print('calculadora de trigonometria!')
        # não fiz :D
    
    def media():
        equation = input('escreva os números para fazer a média: ')

        #vê apenas quantos números há para saber por quanto dividir
        from re import split
        divisor = split(r'[\+\-\*/]', equation.replace(' ', '')) #tira qualquer sinal e espaçamento e transforma em lista
        divisor = len(divisor) #a lista era pra verificar o tamanho e assim achar o divisor

        return eval(equation) / divisor #retorna a média
    
    while True:
            print('tipos de calculadoras: (normal, matriz, trigonometria, média)')
            act = input(f'escolha uma das calculadoras ou digite "voltar": ').lower()

            match act:
                case 'normal':
                    print(f'resultado: {calculadora_normal()}')
                case 'matriz':
                    print(f'resulatdo: {matriz()}')
                case 'trigonometria':
                    print(f'resulatdo: {trigonometria()}')
                case 'média':
                    print(f'resulatdo: {media()}')
                case 'voltar':
                    break
                case _:
                    print('calculadora desconhecida, tente novamente!')

def ajuda():
    #feito para caso o usuário tivesse dúvida para fazer algo no programa
    print('como posso te ajudar ?')
    while True:

        print('Dúvidas conhecidas: \n 1.Como fazer radiciação ?')
        act = input('escolha uma das perguntas ou digite "voltar": ').lower()
        match act:
            case 'voltar':
                break
            case 'como fazer radiciação ?': #para ensinar como fazer radiciação na calculadora normal
                print('Para fazer a radiciação de algum número, na calculadora normal, o eleve pela fração da potência \n' \
                      'Exemplo: a raíz quadrada de 4 --> 4 ** (1/2)')
            case _:
                print('não sei responder isso, desculpe')

print('Calculadora iniciada !')
while True:
    print('ações possíveis: escolher calculadora, ajuda, sair')

    act = input('digite uma das ações: ').lower()
    #usa o "in" ao invés de um match case ou "==" para caso o usuário escreva errado
    #o programa possa ainda sim ter uma chance de entender a ação que o usuário queria

    if 'aj' in act:
        ajuda()

    elif 's' in act:
        break

    elif 'cal' in act:
        escolha_de_calculadora()

    else:
        print('ação inválida, tente novamente!')