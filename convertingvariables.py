import re
from bs4 import BeautifulSoup
import html_to_json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from datetime import datetime

def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False
with open("PATENTES/00028986000108-01.html") as fp:
#with open("00000000000191-01.html") as fp:
    soup = BeautifulSoup(fp,"html5lib")

with open("PATENTES/00028986000108-01.html") as fp:
#with open("00000000000191-01.html") as fp:
    soup2 = BeautifulSoup(fp,"lxml")
# links = []
#for link in soup.findAll('a'):
#    links.append(link.get('href'))
# links = soup.find_all("a")
#
# for link in links:
#    print (link.get('href'))
# print(links)
lista_title=[]
#
taw =soup.table
taw2=soup2.table
# table_MN = pd.read_html(taw2)
# print(table_MN)
for para in taw.find_all("b"):
    lista_title.append(para.get_text())


    #for i in range(len(lista_title)):
print(lista_title)
lista_title.pop()
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
lista_title.pop(0)
text_title=str(lista_title)
text_title_split=(""" """.join(text_title.split()))
text_title_split = text_title_split.replace(r"\n\t","")
text_title_split =text_title_split.replace("[","")
text_title_split =text_title_split.replace("]","")
text_title_split =text_title_split.replace(r"'","")


text_title_split=str(text_title_split)
print(text_title_split)



lista_title_final =text_title_split.split(",")

print(lista_title_final)
pagina_resultado="Páginas de Resultados"
text_test= (soup.table).get_text()
text_split=  (" ".join(text_test.split()))

number1=text_split.find("'")+1
number2=text_split.rfind("'")
Cnpj =text_split[number1:number2]
print(text_split)
listaBR = []
dataBR=[]
br_value= "B"
for i in range(len(text_split)):
    if(text_split[i]==br_value):
        text_to_append=i
        text_to_append2=text_split[i+1]
        text_toappend3=text_split[i+2]
        if text_to_append2=="R" and text_toappend3==" ":
            text_real =text_split[i:i+19]
            listaBR.append(text_real)
            data_real=text_split[i+20:i+30]
            dataBR.append(data_real)
listap=[]
p_value= "P"
dataP=[]
lista_titlep=[]
lista_ipc_p=[]
for i in range(len(text_split)):
    if(text_split[i]==p_value):
        text_to_append=i
        text_to_append2=text_split[i+1]
        text_toappend3=text_split[i+2]
        if text_to_append2=="I" and text_toappend3==" ":
            text_real =text_split[i:i+12]
            if not text_real =='PI [ Início ':
                listap.append(text_real)
                data_real = text_split[i + 13:i + 23]
                dataP.append(data_real)


                if data_valida(data_real) is True :
                    text_title_provisory=text_split[i+24:i+42]
                    str_match =[s for s in lista_title_final if text_title_provisory in s]
                    print(str_match)

                    # text_ipcp=text_split[number_ipc:+8]
                    # print(text_ipcp)
                    for j in range(len(str_match)):
                        if not str_match[j] in lista_titlep:
                            lista_titlep.append(str_match[j])
                            number_toappend_ipc=len(str(str_match[j]))
                            text_title_for_now = str(str_match[j])
                            text_title_for_now=text_title_for_now[1:number_toappend_ipc-1]
                            finding_Text= text_split.find(text_title_for_now)

                            numberf_ipc_inicio=finding_Text+number_toappend_ipc-1
                            numberf_ipc_final =finding_Text+number_toappend_ipc+9
                            texto_achado=text_split[numberf_ipc_inicio:numberf_ipc_final]
                            print("ipc",texto_achado)
                            lista_ipc_p.append(texto_achado)
                            #



                            # ipc_to_append_p= text_split[i+ipc_to_calculator:ipc_to_calculator+8]
                            # lista_ipc_p.append(ipc_to_append_p)



# for k in range(len(lista_titlep)):
#     number=len(lista_titlep[k])
#     text_title_for_now=lista_titlep[k]
#     finding_Text= text_split.find(text_title_for_now)
#     print(finding_Text)
#     text_toappendipp=text_split[finding_Text+number:finding_Text+number+8]
#     print(text_toappendipp)
listam=[]
m_value="M"
dataM=[]
for i in range(len(text_split)):
    if(text_split[i]==m_value):
        text_to_append=i
        text_to_append2=text_split[i+1]
        text_toappend3=text_split[i+2]
        if text_to_append2=="U" and text_toappend3==" ":
            text_real =text_split[i:i+12]
            listam.append(text_real)
            data_real = text_split[i + 13:i + 23]
            dataM.append(data_real)

print(listaBR)
print(dataBR)
print(f"A lista{listap}")
print(dataP)
# lista_titlep=set(lista_titlep)

print(f"A lista p title{lista_titlep}")
print(len(lista_titlep))
print(lista_ipc_p)
print(listam)
print(dataM)






print(Cnpj)










#
#
#
#
#
#
#
# output_json = html_to_json.convert(taw)
# print(output_json)

