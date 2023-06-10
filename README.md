# Documentação da Função Lambda AgeOfFamousPeople
## Descrição de como utilizar a Função Lambda
A função Lambda 'AgeOfFamousPeople' busca o nome de um famoso de acordo com a idade informada caso exista no código.

## Saída Esperada
Será informada uma idade e ela será processada, caso exista um famoso no código com a idade digitada, será retornado o nome do famoso. Caso não exista será retornada uma mensagem informado o caso.

## Entrada
"idade": alguma idade em número
## Saída:
"resultado": Nome do famoso de acordo a idade informada
## Exemplo de resposta:

``{
    "resultado": "Angelina Jolie"
}
``

## Dependências Externas
A função Lambda AgeOfFamousPeople não possui dependências externas além dos serviços nativos da AWS.

## Instruções para Execução
Acesse o console da AWS (https://aws.amazon.com) e faça login na sua conta.
Navegue até o serviço AWS Lambda.
Selecione a função Lambda AgeofFamousPeople.
Verifique se as configurações e os gatilhos da função estão corretamente configurados.
Para testar a função, clique no botão "Teste" na parte superior da página.
Selecione ou crie um evento de teste.
Clique em "Testar" para executar a função Lambda.
## Testes e Depuração
Para testar a função Lambda adequadamente, siga as instruções de execução fornecidas acima.

Para depurar a função Lambda, você pode usar os recursos de log do AWS Lambda. Os logs fornecerão informações detalhadas sobre a execução da função, incluindo mensagens de erro, registros de eventos e quaisquer outras saídas de registro adicionais que você tenha incluído no código.
