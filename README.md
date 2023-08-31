# Desafio-dio-bank-account

## Conta Bancária
Este é um simples programa em Python que simula uma conta bancária. Ele define a classe ContaBancaria que possui métodos para realizar operações de depósito e saque, bem como verificar o saldo disponível.

## Funcionamento
O programa começa solicitando ao usuário o nome do titular da conta e o saldo inicial da conta. Em seguida, cria uma instância da classe ContaBancaria com essas informações.

Após isso, o usuário é solicitado a inserir um valor para depósito e, em seguida, o método cliente_deposito é chamado para adicionar esse valor ao saldo da conta.

Da mesma forma, o usuário é solicitado a inserir um valor para saque e, em seguida, o método cliente_saque é chamado para deduzir esse valor do saldo da conta. Se o saldo for insuficiente para o saque, uma mensagem apropriada será exibida.

Por fim, o saldo disponível na conta é obtido através do método ObterSaldo e é exibido ao usuário.

## Como Usar
  1. Clone ou faça o download deste repositório.
  2. Execute o arquivo Python em um ambiente que suporte a linguagem, como um terminal ou ambiente de desenvolvimento Python.


## Gerenciamento Bancário V.2
Este programa em Python implementa um sistema simples de gerenciamento bancário com interface de menu. Os usuários podem realizar ações como depósito, saque, visualização de extrato, criação de contas e listagem de contas existentes.

## Funcionalidades
  1. Depósito: Permite aos usuários depositar fundos em suas contas, atualizando o saldo e o histórico de transações.

  2. Saque: Usuários podem sacar dinheiro, respeitando limites de saldo e transações. Verificações são feitas para garantir limites aceitáveis.

  3. Extrato: Usuários podem visualizar o extrato da conta, mostrando histórico e saldo atual.

  4. Criação de Usuário: Criação de perfis de usuário com informações pessoais, como nome, data de nascimento e endereço.

  5. Criação de Conta: Usuários existentes podem criar novas contas, associando-as a perfis. Contas são numeradas e rastreadas.

  6. Listagem de Contas: Lista todas as contas criadas, mostrando número, usuário e saldo.

## Uso
  1. Execute o script.
  2. Escolha uma opção no menu digitando a letra correspondente e pressionando Enter.
  3. Siga as instruções da opção escolhida, por exemplo, para depositar, insira o valor.
## Obs: O sistema impõe limites para saques por conta (LIMITE_SAQUES) e verifica a elegibilidade baseada no saldo e limites.
