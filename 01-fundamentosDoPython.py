#
# nome = 'Reinaldo Junior' #string
# idade = 39  #integer
# altura = 1.89  #float
# mensagem = 'Bom dia!'  #string
# professor = True  #Boolean
#
#
# print('meu nome é:',nome,'\n' 'minha idade é:' ,idade,'\n' 'eu tenho:',altura, 'de altura''\n' 'tenha um' ,mensagem)


# nome = input('Digite o seu nome: ')
# idade = input('Digite a sua idade: ')

# print('O nome digitado foi:', nome)
# print('O idade digitada foi:', idade)

# print('Olá', nome + ', você tem', idade, 'anos.')


# f-string
# nome = input('Digite o seu nome: ')
# idade = input('Digite a sua idade: ')
# fruta_favorita = input('Qual é a sua fruta favorita? ')
#
# print(f' Olá {nome}, você tem {idade} anos de idade e a sua fruta favorita é {fruta_favorita}')

# nome = input('Digite o seu nome: ')
# idade = int(input('Digite a sua idade: '))
# print(f'Olá {nome}, daqui 5 anos voce terá {idade + 5} anos de idade ')
#
# # print(type(nome))
# # print(type(idade))

## Operadores Aritimeticos
# numero1 = 10
# numero2 = 3
#
# print(numero1 + numero2)
# print(numero1 - numero2)
# print(numero1 * numero2)
# print(numero1 / numero2)
# print(numero1 // numero2)
# print(numero1 % numero2)
# print(numero1 ** numero2)


# preco = 50  # valor em R$
# desconto = 10  # Desconto em %
#
# preco = float(input('Digite o valor do produto: R$'))
# desconto = float(input('Digite o valor do desconto em Porcentagem: '))
#
# precoComDesconto = preco - (preco * desconto / 100)
# print(f'O Valor com desconto é de R${precoComDesconto}')


# quant_produto = int(input('Digite a quantidade do produto: '))
# uso_diario = int(input('Digite a quantidade usada do produto diariamente: '))
#
# duracao_produto = int( quant_produto / uso_diario )
#
# print(f'O Produto irá durar {duracao_produto} dias')
# print(f'O Produto irá durar {duracao_produto:.0f} dias')


## Operadores Relacionais
# num1 = 10
# num2 = 11
#
# print( num1 == num2 )
# print( num1 != num2 )
# print( num1 > num2 )
# print( num1 < num2 )
# print( num1 >= num2 )
# print( num1 <= num2 )


# idade = int(input('Digite sua idade: '))
# verificador = idade >= 18
# print(verificador)


## Operadores Logicos
# Para dirigir a pessoa tem que ser maior que 18 anos e ter carteira de motorista
# idade = int(input('Digite sua idade: '))
# carteira = True
#
# verificador = idade >= 18 and carteira == True
#
# print(verificador)


## Condicionais ( if, else )
# numero = int(input('Digite um numero: '))
#
# if numero == 10:
#     print('Acertou o numero', numero)
# else:
#     print('Voce errou o numero')


# idade = int(input('Digite sua idade: '))
# if idade >= 18:
#     print('Maior de idade')
# else:
#     print('Menor de idade')


# nota_aluno = float(input('Qual foi a sua nota no exame? '))
#
# if nota_aluno >=7:
#     print('Aluno Aprovado com nota: ', nota_aluno)
# else:
#     print('Aluno Reprovado com nota: ', nota_aluno)


# nota_aluno = float(input('Qual foi a sua nota no exame? '))
#
# if nota_aluno >= 7:
#     print('Aluno Aprovado com nota: ', nota_aluno)
#
# elif nota_aluno >= 5 or nota_aluno > 7:
#     print('Aluno em recuperação com nota: ', nota_aluno)
#
# else:
#     print('Aluno Reprovado com nota: ', nota_aluno)


# usuario = input('Digite o seu usuario: ')
# senha = input('Digite sua senha: ')
#
# if usuario == 'Admin' and senha == '123Admin':
#     print('Suceso, Login Permitido!')
#     print('Pode abrir a aplicação')
# else:
#     print('Erro, Verifique o usuario ou senha')


# idade = int(input('Digite sua idade: '))
# autorizacao_pais = input('você tem autorização dos pais?: (s/n): ')
#
# if idade >= 18:
#     print('Acesso permitido')
# elif idade >= 16 and autorizacao_pais == 's':
#     print('Acesso permitido com autorização dos pais')
# else:
#     print('Acesso Negado')


## Condicionais ( for, while )
# for i in range(5, 0, -2):
#     print(i)


# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# senha = '';
# while senha != '123':
#     senha = input('Qual é senha do sistema? ')
#
# print ('Acesso liberado')


# ## Listas, Tuplas, Dicionarios
# frutas = ['Abacate', 'Banana', 'Morango']
#
# # print(frutas[2]) # Baseado em index, sempre inicia no zero
#
# # Adiciona no final da lista
# frutas.append('Uva')
# frutas.append('Laranja')
#
# # Remove da lista
# frutas.remove('Banana')
#
# # Mostra tamanho da lista
# print(len(frutas))
#
# print(frutas)


# tarefas = []
#
# tarefas.append('Estudar Python com IA')
# tarefas.append('Ler um artigo sobre IA')
# tarefas.append('Responder emails')
# tarefas.append('Lavar o carro')
#
# # print('Minhas tarefas diarias')
# # print(tarefas[0])
# # print(tarefas[1])
# # print(tarefas[2])
#
# print('Minhas tarefas de hoje ')
# for tarefa in tarefas:
#     print(f'Tarefa: {tarefa}')


# # Tuplas são usadas para dados que não são mudados / não podem mudar
# meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho' 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' )
#
# print(meses[1])


## Dicionarios -> Usuarios, Endereços, Produtos, Configurações etc.
# usuario = {
#     'Nome': 'Reinaldo',
#     'Idade': 39,
#     'Departamento': 'TI'
# }
#
#
# usuario['Idade'] = 40
# usuario['Cidade'] = 'Salvador'
#
#
#
# print(usuario)

#
# aluno = {
#     'Nome': input('Nome do Aluno: '),
#     'Idade': input('Idade do Aluno: '),
#     'Nota': float(input('Nota do Aluno: '))
# }
#
# print(f'{aluno['Nome']} tem {aluno['Idade']} anos de idade, e tirou a nota de {aluno['Nota']}')


## Funções
# def saudacao(nome, idade):
#     print(f' Olá {nome}!, Você tem {idade} anos de idade, Vamos aprender AI?')
#
# saudacao('Reinaldo Junior', 39)
# saudacao('Maria', 25)

# def somar( num1, num2):
#     return num1 + num2
#
# resultado = somar(50, 30)
# print(f'O Resultado da soma é de: {resultado}')


def calcular_desconto(preco, porcentagem):
    return preco - ( preco * porcentagem / 100 )

valor_final = calcular_desconto(1010, 25)
print(f'O Valor final com o desconto é de R${valor_final:.2f}')

















