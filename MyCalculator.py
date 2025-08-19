def escolha_de_calculadora():

    def calculadora_normal():
        return eval(input('digite a operação: ')) #analisa a equação e já entrega o resultado

    def matriz():
        print('Calculadora de matriz 3x3')
        from numpy import linalg, array
        def matrix3x3():
            #linhas da matriz
            l1 = []
            l2 = []
            l3 = []

            lines = [l1, l2, l3]
            #insere os números em cada linha
            for i, line in enumerate(lines):
                numeros = input(f'Digite os números da linha {i + 1} separados por espaço: ').split()
                line[:] = [int(n) for n in numeros]  # converte para int e substitui conteúdo

                lines = array(lines)
                return(round(linalg.det(lines)))

        def matrix4x4():
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            lines =[l1, l2, l3, l4]
            for i, line in enumerate(lines):
                numeros = input(f'Digite os números da linha {i + 1} separados por espaço: ').split()
                line[:] = [int(n) for n in numeros]  # converte para int e substitui conteúdo

                lines = array(lines)
                return(round(linalg.det(lines)))

        act = input('escolha matriz "3x3" ou "4x4": ')

        if '3' in act:
            return(matrix3x3())
        if '4' in act:
            return(matrix4x4())


    def trigonometria():
        print('calculadora de trigonometria!')

        op = input('digite os números correspondentes à "a" "b" e "c" separados por espaço: ').split()
        a = float(op[0])
        b = float(op[1])
        c = float(op[2])

        delt = b**2 - 4 * a * c

        x1 = (-b + delt ** (1/2)) / 2 * a
        x2 = (-b - delt ** (1/2)) / 2 * a

        if delt == 0 :
            return x1
        elif delt < 0:
            return 'delta negativo, número complexo !'
        else:
            return x1, x2
    
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