#coding: utf-8

def ComissaoSalario():
    Nome = input("Entre com o nome do vendedor: ")
    Salariofixo = float(input("Informe o salário: "))
    Vendas = float(input("Informe o total de vendas: "))
    Comissao = 0.15*Vendas 
    Pagamentoesperado=Salariofixo+Comissao
    return Nome,Comissao, Pagamentoesperado


if __name__=="__main__":
    Nome,Comissao, Pagamentoesperado =ComissaoSalario() 
    strg = "{0} obteve R$ {1:.2f} de comissao e vai receber {2:.2f}".format(Nome,Comissao,Pagamentoesperado)
    print(strg)