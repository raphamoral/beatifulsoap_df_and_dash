from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import PATENTES
from dash import Dash, dash_table
import dash



    #htmls = [arq for arq in lista_pasta if arq.lower().endswith(".html")]
    #print(htmls)
def contem_itens(file):
    with open(file) as fp:

        soup = BeautifulSoup(fp,"html5lib")

    soup=soup.table
    numberofresults = soup.find_all("div", id="tituloEResumoContextGlobal", class_="context")
    numberofresults = soup.find_all("b")






    numbertoappend = (numberofresults[2]).text



    lista_titlea=[]
    lista_ipca=[]
    lista_pedidoa=[]
    lista_dataa=[]
    for link in soup.find_all("td" and not "b",align="center"):
        variable_text= link.text
        variable_text=""" """.join(variable_text.split())
        if len(variable_text) > 10:

            lista_pedidoa.append(variable_text)
        else:

             lista_dataa.append(variable_text)
    for link in soup.find_all("td" and not "b",align="left"):
        variable_text= link.text
        variable_text=""" """.join(variable_text.split())
        if len(variable_text)>10:

            lista_titlea.append(variable_text)
        elif variable_text =="":
            pass
        else:

            lista_ipca.append(variable_text)



    cpf = str(lista_titlea[2])[27:45].replace(r"'", "")


    lista_cpfa=[]
    lista_filea=[]
    lista_resultadoa=[]

    for i in range(len(lista_ipca)-1):
        lista_filea.append(file)

    for i in range(len(lista_ipca)-1):
        lista_cpfa.append(cpf)
    lista_dataa.pop(0)
    lista_dataa.pop(0)
    lista_dataa.pop(0)
    lista_dataa.pop(0)


    lista_titlea.pop(0)
    lista_titlea.pop(0)
    lista_titlea.pop(0)
    lista_titlea.pop(-1)
    if len(lista_pedidoa)!=len(lista_titlea):
        for i in range(len(lista_titlea),len(lista_pedidoa)-1):

            lista_titlea.append("-")

    if len(lista_ipca)>len(lista_titlea):
        number_to_pop=len(lista_ipca)-len(lista_titlea)
        for i in range(0,number_to_pop):
            lista_ipca.pop(-1)





    lista_pedidoa.pop(0)
        #print(lista_pedido)
        #print(lista_data)



    for i in range(len(lista_ipca)):
        lista_resultadoa.append(numbertoappend)


    return lista_filea, lista_cpfa, lista_resultadoa, lista_pedidoa, lista_dataa, lista_titlea, lista_ipca

def itens_vazio(file):
        with open(file) as fp:
            soup = BeautifulSoup(fp, "html5lib")
        lista_titlea = ["-"]
        lista_ipca = ["-"]
        lista_pedidoa = ["-"]
        lista_dataa = ["-"]
        lista_CPF_do_Zero = []
        for link in soup.find_all("div", align="left"):
            variable_text = link.text
            variable_text = """ """.join(variable_text.split())
            lista_CPF_do_Zero.append(variable_text)

        cpf = lista_CPF_do_Zero[1][40:58].replace(r"'", "")
        lista_cpfa=[f"{cpf}"]
        lista_resultadoa=["0"]
        lista_filea=[f"{file}"]
        print("file", file
              )
        print(lista_filea)
        print(lista_cpfa)
        print(lista_resultadoa)
        print(lista_pedidoa)
        print(lista_dataa)
        print(lista_titlea)
        print(lista_ipca)


        return lista_filea, lista_cpfa, lista_resultadoa, lista_pedidoa, lista_dataa, lista_titlea, lista_ipca






lista_pasta = os.listdir()
lista_pasta.pop()
lista_file =[]
lista_cpf =[]
lista_resultado =[]
lista_pedido =[]
lista_data =[]
lista_title =[]
lista_ipc =[]
lista_de_Dfs=[]
for i in range(len(lista_pasta)):
    file =lista_pasta[i]
    with open(file) as fp:
        # with open("00000000000191-01.html") as fp:
        soup = BeautifulSoup(fp, "html5lib")
        soup= soup.text
        text_to_find ="Nenhum resultado foi encontrado para a sua pesquisa"

        if text_to_find in soup:
            lista_filea, lista_cpfa, lista_resultadoa, lista_pedidoa, lista_dataa, lista_titlea, lista_ipca=itens_vazio(file)
        else:
            lista_filea, lista_cpfa, lista_resultadoa, lista_pedidoa, lista_dataa, lista_titlea, lista_ipca=contem_itens(file)

        lista_file+=lista_filea
        lista_cpf+=lista_cpfa
        lista_resultado+=lista_resultadoa
        lista_pedido+=lista_pedidoa
        lista_data+=lista_dataa
        lista_title+=lista_titlea
        lista_ipc+=lista_ipca

df = pd.DataFrame(
            list(zip(lista_file, lista_cpf, lista_resultado, lista_pedido, lista_data, lista_title, lista_ipc)),
            columns=['Arquivo', 'CPNJ', "RESULTADO", "NÚMERO DO PEDIDO", "Data do Depósito", "Título", "IPC"])

print(df)


# 
#
app = Dash(__name__)
#
app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
#
if __name__ == '__main__':
     app.run_server(debug=True)