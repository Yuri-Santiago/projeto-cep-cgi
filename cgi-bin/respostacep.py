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

cep = form.getvalue('cep')


request = requests.get(f'https://viacep.com.br/ws/{cep}/json')

try:
    response = request.json()
    if response.get('erro', False):
        conteudo = """
                   <div class="limiter">
                   <div class="container-login100">
                   <div class="wrap-login200 p-b-50 p-t-50">
                   <h1 class="cor-preta">O CEP digitado não existe</h1>
                   <a href="./cep.py" class="btn btn-lg cor-preta fundo-azul" role="button">Voltar</a>
                   </div>
                   </div>
                   </div>
                   """
    else:
        conteudo = """
                   <div class="limiter">
                   <div class="container-login100">
                   <div class="wrap-login200 p-b-50 p-t-50">
                   <h1 class="cor-preta">CEP Encontrado</h1>
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
                   <tr>
                   <th scope="row">Resultado</th>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   </tr>
                   </tbody>
                    </table>
                    <a href="./cep.py" class="btn btn-lg cor-preta fundo-azul" role="button">Voltar</a>
                    </div>
                    </div>
                    </div>
                   """ % (response['uf'], response['localidade'], response['bairro'], response['logradouro'], response['cep'])

except:
    conteudo = """
               <div class="limiter">
               <div class="container-login100">
               <div class="wrap-login200 p-b-50 p-t-50">
               <h1 class="cor-preta">Número de Dígitos Errado</h1>
               <a href="./cep.py" class="btn btn-lg cor-preta fundo-azul" role="button">Voltar</a>
               </div>
               </div>
               </div>
               """
func.corpo(conteudo)
