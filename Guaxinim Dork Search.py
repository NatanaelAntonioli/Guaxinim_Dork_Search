#MIT License
#
#Copyright (c) 2017 Natanael Antonioli
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import webbrowser
url = "https://www.google.com.br/search?q="
data = ""
buscar = False
a=  """

     _____ _    _        __   _______ _   _ _____ __  __     _____   ____  _____  _  __     _____ ______          _____   _____ _    _ 
    / ____| |  | |  /\   \ \ / |_   _| \ | |_   _|  \/  |   |  __ \ / __ \|  __ \| |/ /    / ____|  ____|   /\   |  __ \ / ____| |  | |
   | |  __| |  | | /  \   \ V /  | | |  \| | | | | \  / |   | |  | | |  | | |__) | ' /    | (___ | |__     /  \  | |__) | |    | |__| |
   | | |_ | |  | |/ /\ \   > <   | | | . ` | | | | |\/| |   | |  | | |  | |  _  /|  <      \___ \|  __|   / /\ \ |  _  /| |    |  __  |
   | |__| | |__| / ____ \ / . \ _| |_| |\  |_| |_| |  | |   | |__| | |__| | | \ \| . \     ____) | |____ / ____ \| | \ \| |____| |  | |
    \_____|\____/_/    \_/_/ \_|_____|_| \_|_____|_|  |_|   |_____/ \____/|_|  \_|_|\_\   |_____/|______/_/    \_|_|  \_\\______|_|  |_|

                            .-.
               .-"` .`'.    /\\|  PROGRAMADO POR: NATANAEL ANTONIOLI
       _(\-/)_" ,  .   ,\  /\\\/  INSCREVA-SE: FÁBRICA DE NOOBS
      {(#o^o#)} .   ./,  |/\\\/   
      `-.(Y).-`  ,  |  , |\.-`             
           /~/,_/~~~\,__.-`                 
          ////~    // ~\\                   
         ==`==`   ==`   ==`

         """
print (a)
print (" ")
print ("----- OPERAÇÕES DE DORKS ---------------------")
print (" ")
print ("1 - Buscar dentro de um site")
print ("2 - Buscar determinado tipo de arquivo")
print ("3 - Buscar em uma URL")
print ("4 - Buscar no conteúdo da página")
print ("5 - Buscar no título da página")
print ("6 - Termo adicional")
print (" ")
print ("----- FILTRAR POR DATA -----------------------")
print (" ")
print ("7 - Na última hora")
print ("8 - Nas últimas 24 horas")
print ("9 - Na última semana")
print ("10 - No último mês")
print ("11 - No último ano")
print ("12 - Qualquer data")
print (" ")
print ("----- COMANDOS -------------------------------")
print (" ")
print ("13 - Realizar busca!")
print ("14 - Zerar parâmetros")
print ("15 - Sair")
print (" ")


while buscar == False:
    print (" ")
    menu = int(input("O que deseja fazer?"))
    print (" ")

    # DEFINE A DATA DO ESCOPO DA BUSCA, INFORMAÇÃO ÚNICA
   
    if menu ==7:
        data= "&tbs=qdr:h"
        
    if menu ==8:
        data= "&tbs=qdr:d"

    if menu ==9:
        data= "&tbs=qdr:w"

    if menu ==10:
        data= "&tbs=qdr:m"

    if menu ==11:
        data= "&tbs=qdr:y"
        
    if menu ==12:
        data= ""
        
    # FUNÇÕES CORE
    
    if menu ==13:
        webbrowser.open(url+data)
        url = "https://www.google.com.br/search?q="
        data = ""
        print ("Busca realizada! Já pode inserir critérios para nova busca.")
        
        
    if menu ==14:
        url = "https://www.google.com.br/search?q="
        data = ""

    if menu==15:
        buscar = True

    # DEFINE OS DORKS DA BUSCA, INFORMAÇÕES SOMADAS
    
    if menu ==1:
        url += "+"
        url += "site:"
        dork = str(input("Insira o site desejado: "))
        url += dork
        print ("Critério Adicionado!")
        print (" ")

    if menu ==2:
        url += "+"
        url += "filetype:"
        dork = str(input("Insira a extensão de arquivo desejada: "))
        url += dork
        print ("Critério Adicionado!")
        print (" ")

    if menu ==3:
        url += "+"
        url += "inurl:"
        dork = str(input("Insira a URL desejada: "))
        url += dork
        print ("Critério Adicionado!")
        print (" ")
        
    if menu ==4:
        url += "+"
        url += "intext:"
        dork = str(input("Insira o texto desejado: "))
        url += dork
        print ("Critério Adicionado!")
        print (" ")

    if menu ==5:
        url += "+"
        url += "intitle:"
        dork = str(input("Insira o texto desejado: "))
        url += dork
        print ("Critério Adicionado!")
        print (" ")
        
    if menu ==6:
        url += "+"
        dork = str(input("Insira o termo desejado:"))
        url += dork
        print ("Critério Adicionado!")
        print (" ")

