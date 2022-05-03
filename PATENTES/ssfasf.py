from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import PATENTES
from dash import Dash, dash_table
import dash

file="00005275000118-01.html"

with open(file) as fp:
    # with open("00000000000191-01.html") as fp:
    soup = BeautifulSoup(fp, "html5lib")


lista_CPF_do_Zero=[]
for link in soup.find_all("div",align="left"):
    variable_text = link.text
    variable_text = """ """.join(variable_text.split())
    lista_CPF_do_Zero.append(variable_text)
cpf=lista_CPF_do_Zero[1][40:58].replace(r"'", "")
print(cpf)
