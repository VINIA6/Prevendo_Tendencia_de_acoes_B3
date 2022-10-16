from chave import chave_api
import requests
import pprint
import pandas as pd 
from io import StringIO

chave_api = 'NMKGPCZ0A2H5Z7FC'

#No plano gratuito só conseguimos fazer 5 requisições por minuto. 
def request_api_times(company,timeserires,chave,mode):
    data_geral = pd.DataFrame()
    for i in company:
        url = f'https://www.alphavantage.co/query?function={timeserires}&symbol={i}&apikey={chave}&datatype={mode}'
        r = requests.get(url)
        if mode == 'json':
            data = r.json()
            # pprint.pprint(data)
            return(data)
        else:
            data = pd.read_csv(StringIO(r.text),sep=',')
            data_geral = pd.concat([data_geral,data])
            
    return data_geral
    