#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb

import func

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
func.cabecalho("Consultar Endereço")
func.corpo("""
           <body>
           <div class="limiter">
           <div class="container-login100">
           <div class="wrap-login100 p-b-160 p-t-50">
           <form class="login100-form validate-form" action="respostaendereco.py" method="post">
           <span class="login100-form-title p-b-43">
           Insira o Endere&ccedil;o
           </span>
           <div class="wrap-input200 rs3 validate-input" data-validate = "Insira o UF">
           <input class="input100" type="text" name="uf">
           <span class="label-input100">Sigla do UF (Ex: CE, SP)</span>
           </div>
           <div class="wrap-input200 rs2 validate-input" data-validate = "Insira a Cidade">
           <input class="input100" type="text" name="cidade">
           <span class="label-input100">Cidade (Ex: Fortaleza, São Paulo)</span>
           </div>
           <div class="wrap-input100 rs4 validate-input" data-validate = "Insira o Logradouro">
           <input class="input100" type="text" name="logradouro">
           <span class="label-input100">Logradouro (Ex: Avenida 13 de Maio)</span>
           </div>
           <div class="container-login100-form-btn">
           <button class="login100-form-btn">
           Buscar Endereço
           </button>
           </div>
           <div class="text-center w-full p-t-23">
           <a href="./cep.py" class="txt1">
           Buscar por CEP
           </a>
           </div>
           </form>
           </div>
           </div>
           </div>
           """)
