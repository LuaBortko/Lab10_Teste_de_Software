# Exercicio 3

## a) Quais testes atuais contradizem as regras? O que fazer com eles antes de mudar o código

- test_cupom_dez: Subtotal 5000, abaixo do mínimo de 10000, não deve receber desconto.

- test_adicionar_apos_cupom: Subtotal final 2000, abaixo do mínimo, não deve receber desconto.

É preciso mudar primeiro os testes para depois mudar o código

## c) No Refactor, guarde a porcentagem e o mínimo juntos em CUPONS. O que mostra que nada mudou

## d) Que valores de quantidade você testou? Por quê?
