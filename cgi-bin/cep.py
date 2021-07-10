#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb

import func

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
func.cabecalho("Consultar CEP")
func.corpo("""
           <div class="limiter">
           <div class="container-login100">
           <div class="wrap-login100 p-b-160 p-t-50">
           <form class="login100-form validate-form" action="respostacep.py" method="post">
           <span class="login100-form-title p-b-43">
           Insira o CEP
           </span>
           <div class="wrap-input100 rs1 validate-input" data-validate = "Insira o CEP">
           <input class="input100" type="text" name="cep">
           <span class="label-input100">CEP com 8 caracteres juntos (Ex: 12345678)</span>
           </div>
           <div class="container-login100-form-btn">
           <button class="login100-form-btn">
           Buscar CEP
           </button>
           </div>
           <div class="text-center w-full p-t-23">
           <a href="./endereco.py" class="txt1">
           Buscar por Endereço
           </a>
           </div>
           </form>
           </div>
           </div>
           </div>
           """)
