# https://faker.readthedocs.io/en/master/index.html
# https://faker.readthedocs.io/en/master/locales/pt_BR.html
# pip3 install faker
from faker import Faker

fake = Faker("pt_BR")  # Configura o Faker para a região do Brasil

# Gera as informações
nome = fake.name()
sobrenome = fake.last_name()
senha = fake.password()
cpf = fake.cpf()
rg = fake.rg()
telefone = fake.phone_number()
celular = fake.cellphone_number()
email = fake.email()
cep = fake.postcode()
endereco = fake.street_address()
bairro = fake.bairro()
cidade = fake.city()
estado_sigla = fake.estado_sigla()

# Imprime as informações geradas
print("Nome:", nome + ' ' + sobrenome)
print("CPF:", cpf)
print("RG:", rg)
print("Telefone:", telefone)
print("Celular:", celular)
print("Email:", email)
print("Senha: ", senha)
print("CEP:", cep)
print("Endereço:", endereco)
print("Bairro:", bairro)
print("Cidade:", cidade)
print("Estado Sigla:", estado_sigla)
