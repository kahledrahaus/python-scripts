# -*- coding: utf-8 -*-
desc_metodo = '''Método dos Potes

Primeiro pote - Gastos fixos

No primeiro potinho será reservado 60% do seu orçamento, com ele você poderá gastar suas despesas diárias e pagamentos
de contas mensais fixas, como quitar dívidas, pagar internet, luz, água, aluguel, e etc.

Segundo Pote - Aposentadoria

Aqui estará reservado 15% do seu dinheiro, deve ser utilizado para seu futuro. Você deve guardar essa porcentagem na
poupança, ou fazer algum investimento confiável, e só tirar quando estiver independente financeiramente.

Terceiro Pote - Fundo de emergência

O terceiro pote também conta com 10% da sua renda, só que esse dinheiro deve ser utilizado em situações de emergência
ou seja, aquelas em que você precisa do dinheiro rápido como em casos de doença, acidentes ou viagem inesperada.

Quarto Pote - Educação

Outra reserva de 10%, só que dessa vez o importante é sua educação. Esse dinheiro deve ser gasto para seu crescimento
profissional e pessoal, com ele você pode fazer cursos, palestras, comprar livros… Enfim, é um gasto para expandir
sua mente.

Quinto Pote - Diversão/Férias/Satisfação pessoal

Essa reserva de 10% deve ser realizada para comprar coisas que melhorem sua vida pessoal, como um carro mais novo,
uma TV nova, a mensalidade da academia ou serviço de streaming, uma viagem sozinho ou em família, etc.

Sexto Pote - Presentes/Caridade

Os últimos 5% que sobraram devem ser guardados para presentes e caridade. Sempre que estiver chegando a data de
alguma comemoração, você pode tirar esse dinheiro para presentear o sortudo. Caso deseje ajudar alguma organização,
esse também é o pote certo.

Modifique de acordo com suas necessidades!
'''

print(desc_metodo)
renda = input("\n\nDigite a sua renda mensal: ")
renda = renda.replace('.', '').replace(',', '.')  # Remova pontos de milhares e substitua vírgula por ponto
renda = float(renda)  # Converta a renda para float

gastos_fixos = renda * 60 / 100
aposentadoria = renda * 15 / 100
fundo_emergencia = renda * 10 / 100
educacao = renda * 10 / 100
diversao = renda * 10 / 100
doacao = renda * 5 / 100

print("\n\t* Gastos fixos: R$ %.2f." % gastos_fixos + "\n")
print("\t* Aposentadoria: R$ %.2f." % aposentadoria + "\n")
print("\t* Fundo de emergência: R$ %.2f." % fundo_emergencia + "\n")
print("\t* Educação: R$ %.2f." % educacao + "\n")
print("\t* Diversão/Férias/Satisfação pessoal: R$ %.2f." % diversao + "\n")
print("\t* Presentes/Caridade: R$ %.2f." % doacao)
