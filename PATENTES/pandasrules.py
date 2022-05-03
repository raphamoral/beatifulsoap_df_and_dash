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
    #with open("00000000000191-01.html") as fp:
        soup = BeautifulSoup(fp,"html5lib")

    soup=soup.table
    numberofresults = soup.find_all("div", id="tituloEResumoContextGlobal", class_="context")
    numberofresults = soup.find_all("b")
    print("number",numberofresults)





    numberofresults = (numberofresults[2]).text
    print(numberofresults)


    lista_title=[]
    lista_ipc=[]
    lista_pedido=[]
    lista_data=[]
    for link in soup.find_all("td" and not "b",align="center"):
        variable_text= link.text
        variable_text=""" """.join(variable_text.split())
        if len(variable_text) > 10:

            lista_pedido.append(variable_text)
        else:

             lista_data.append(variable_text)
    for link in soup.find_all("td" and not "b",align="left"):
        variable_text= link.text
        variable_text=""" """.join(variable_text.split())
        if len(variable_text)>10:

            lista_title.append(variable_text)
        else:

            lista_ipc.append(variable_text)

        #cpf=str(lista_title[2])
        #cpf=cpf.isdigit()

    cpf = str(lista_title[2])[27:45].replace(r"'", "")

    print("CPF",cpf)
    lista_cpf=[]
    lista_file=[]
    lista_resultado=[]
    for i in range(len(lista_ipc)):
        lista_file.append(file)

    for i in range(len(lista_ipc)):
        lista_cpf.append(cpf)

    print(len(lista_cpf))
    print(len(lista_ipc))
    lista_title.pop(0)
    lista_title.pop(0)
    lista_title.pop(0)
    #print(lista_title)
        #print(lista_ipc)
    lista_pedido.pop(0)
        #print(lista_pedido)
        #print(lista_data)


    for i in range(len(lista_ipc)):
        lista_resultado.append(numberofresults)
    df = pd.DataFrame(
        list(zip(lista_file, lista_cpf, lista_resultado, lista_pedido, lista_data, lista_title, lista_ipc)),
        columns=['Arquivo', 'CPNJ', "RESULTADO", "NÚMERO DO PEDIDO", "Data do Depósito", "Título", "IPC"])
    return df

def itens_vazio(file):
        with open(file) as fp:
            soup = BeautifulSoup(fp, "html5lib")
        lista_title = [""]
        lista_ipc = [""]
        lista_pedido = [""]
        lista_data = [""]
        lista_CPF_do_Zero = []
        for link in soup.find_all("div", align="left"):
            variable_text = link.text
            variable_text = """ """.join(variable_text.split())
            lista_CPF_do_Zero.append(variable_text)
        cpf = lista_CPF_do_Zero[1][40:58].replace(r"'", "")
        lista_cpf=["cpf"]
        lista_resultado=["0"]
        lista_file=[f"{file}"]
        df = pd.DataFrame(
            list(zip(lista_file, lista_cpf, lista_resultado, lista_pedido, lista_data, lista_title, lista_ipc)),
            columns=['Arquivo', 'CPNJ', "RESULTADO", "NÚMERO DO PEDIDO", "Data do Depósito", "Título", "IPC"])
        return df






lista_pasta = os.listdir()
lista_pasta.pop()

lista_de_Dfs=[]
for i in range(len(lista_pasta)):
    file =lista_pasta[i]
    with open(file) as fp:
        # with open("00000000000191-01.html") as fp:
        soup = BeautifulSoup(fp, "html5lib")
        soup= soup.text
        text_to_find ="Nenhum resultado foi encontrado para a sua pesquisa"
        if soup.find("Nenhum resultado foi encontrado para a sua pesquisa")=="-1":
            df=itens_vazio(file)
        else:
            df=contem_itens(file)
        lista_de_Dfs.append[df]

# 
#
# app = Dash(__name__)
#
# app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)