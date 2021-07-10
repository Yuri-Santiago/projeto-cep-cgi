#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import cgitb

import requests

import func

i = 0
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
func.cabecalho("Resposta Endereço")

form = cgi.FieldStorage()

uf = form.getvalue('uf')
cidade = form.getvalue('cidade')
logradouro = form.getvalue('logradouro')

request = requests.get(f'https://viacep.com.br/ws/{uf.upper()}/{cidade.title()}/{logradouro.title()}/json')

try:
    response = request.json()
    if not response:
        raise Exception
    conteudo = """
               <div class="limiter">
               <div class="container-login100">
               <div class="wrap-login200 p-b-50 p-t-50">
               <h1 class="cor-preta">Resultados de CEPs</h1>
               <table class="table table-hover cor-branca">
               <thead>
               <tr>
               <th scope="col">#</th>
               <th scope="col">UF</th>
               <th scope="col">Cidade</th>
               <th scope="col">Bairro</th>
               <th scope="col">Logradouro</th>
               <th scope="col">CEP</th>
               </tr>
               </thead>
               <tbody>
               """
    for d in response:
        i += 1
        conteudo += """
                    <tr>
                    <th scope="row">%d</th>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    </tr>
                    """ % (i, d['uf'], d['localidade'], d['bairro'], d['logradouro'], d['cep'])
    conteudo += """
                </tbody>
                </table>
                <a href="./endereco.py" class="btn btn-lg cor-preta fundo-azul" role="button">Voltar</a>
                </div>
                </div>
                </div>
                """

except:
    conteudo = """
               <div class="limiter">
               <div class="container-login100">
               <div class="wrap-login200 p-b-50 p-t-50">
               <h1 class="cor-preta">O endereço foi digitado errado ou não existe :(</h1>
               <a href="./endereco.py" class="btn btn-lg cor-preta fundo-azul" role="button">Voltar</a>
               </div>
               </div>
               </div>
               """
func.corpo(conteudo)
