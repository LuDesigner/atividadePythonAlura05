<h1>Desafios do Python - Mão na massa: refatorando uma função </h1>

## Obs: Abaixo esta o que foi solicitado nas atividades e muito mais, eu fiz da forma que meus conhecimentos me permitiam naquele momento, acrescentei menu, opções, formas de modificar titular, debito, crédito e muito mais, espero que gostem ^^

##  

A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como título, autor e número de páginas:

```
class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
```

Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

##  

<h1>Desafios do Python - Hora da prática: criando classes, construtores e métodos </h1>

##  Questão 01:
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

##  Questão 02:
Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

##  Questão 03:
Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

##  Questão 04:
Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

##  Questão 05:
Crie uma instância da classe e imprima o valor da propriedade titular.

##  Questão 06:
Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

##  Questão 07:
Crie um método de classe para a conta ClienteBanco.

<div>
  <img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAyMTJfNSAg/MDAxNjQ0NTkzNzE5MzQ1.q5g3zqnCq2Rt1xUmpSFx2xWRQTl4VmngS8FGT7eGD0Ig.UKr_wLSCCg8PD-v8TfDddCKFIWhKoeqh5lZM09FVrsYg.PNG.sw4r/image.png?type=w800">
</div>