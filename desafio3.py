# Informações: Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint, como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.

# Regras do saque:

# - Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
# - Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
# - Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
# - Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.

# Entrada de dados
saldo_total = int(input("Informe o valor do saldo: "))
valor_saque = int(input("Informe o valor do saque: "))

# toDo: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
  novo_saldo = saldo_total - valor_saque
  print(f"Saque realizado com sucesso! Novo saldo: {novo_saldo}")
else:
  print("Saldo insuficiente. Saque não realizado!")