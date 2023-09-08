# Informções: Para esse desafio, considere que você foi contratado por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

saldo_atual = float(input("Informe seu saldo atual: "))
valor_deposito = float(input("Informe o valor do depósito: "))
valor_retirada = float(input("Informe o valor do saque: "))

#toDo: Calcular o saldo atualizado de acordo com a descrição deste desafio.
novo_saldo = saldo_atual + valor_deposito - valor_retirada

#toDo: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f"Saque realizado com sucesso!\nSaldo atualizado na conta:{novo_saldo}")