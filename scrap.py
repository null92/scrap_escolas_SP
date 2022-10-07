import requests
from bs4 import BeautifulSoup
import csv
 
myFile = open('escolas.csv', 'r+')
pagina = 1

while(pagina <= 3113):
    url = 'http://pesquisaseduc.fde.sp.gov.br/localize_escola?pageNumber="{paginas}"&inicial=False'.format(paginas = pagina)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    lines = soup.find_all('article', {'style': 'margin-top: 10px;'})

    for line in lines:
        txt = line.text
        x = txt.replace(" | ", "\n").replace(":  ", ":").replace(": ", ":").replace("     - ", "-").replace(") 000", ")").replace("\n", "").replace("     ", "").replace("Nome da Escola:", "").replace("Tipo de ensino:", ";").replace("Município:", ";").replace("Diretoria de Ensino:", ";").replace("Rede de Ensino:", ";").replace("Endereço:", ";").replace("Bairro:", ";").replace("CEP:", ";").replace("ZONA:", ";").replace("Telefone:", ";").replace("E-mail:", ";")
        x = x.split(';')
        writer = csv.writer(myFile)
        writer.writerow(x)
    pagina += 1

myFile.close()