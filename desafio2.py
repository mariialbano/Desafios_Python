# Informações: Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Informe a quantidade de ativos: "))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input("Informe o ativo: ")
    ativos.append(codigoAtivo)

#toDo: Ordenar os ativos em ordem alfabética.
ativos.sort()

#toDo: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
  print(ativo)