import requests
from requests.auth import HTTPBasicAuth
import json
import xml.etree.ElementTree as ET
from requests.adapters import HTTPAdapter, Retry
import time

#REFERENCIAS 
#https://docs.openkm.com/kcenter/view/okm-6.4/download-document-with-direct-link.html

class OpenKm():
    end_point_base = 'http://65.21.188.116:8080/OpenKM/services/rest/search/find?property=okp:encCobro.'
    def get_auth_creds(self):
        return HTTPBasicAuth('usrocr', 'j2X7^1IwI^cn')

    def get_response(self,_url):
        _headers = {
            'Accept': 'application/json',
        }
        response = requests.get(_url,headers =_headers, auth = self.get_auth_creds())
        return response

    #FUNCION PARA DESCARGAR ARCHIVO pdf por UIID 
    def download_doc(self,uuid = None):
        user = 'usrocr'
        passwd = 'j2X7^1IwI^cn'
        url = "http://65.21.188.116:8080/OpenKM/services/rest/document/getContent?docId={}" .format(uuid)
        response = requests.get(url, auth = self.get_auth_creds())
        status_code = response.status_code
        if (status_code in range(200,399)):
            print("Se a descargado ")
            return response
        else:
            return "F => {} ".format(status_code)
            
    def get_doc_by_folio(self,_query = None):
        _metadata = 'folio'
        url = "{}{}={}" .format(self.end_point_base,_metadata,_query)
        response = self.get_response(url)
        status_code = response.status_code
        if (status_code in range(200,399)):
            print("Codigo de estado es aceptable") 
            data = response.json()  
            data_node = data['queryResult']['node']
            path,uuid = data_node['path'],data_node['uuid']
            print("DATA => PATH: {} /n UUID: {}" .format(path,uuid))
            return uuid
        else:
            return "ERROR "



openkm = OpenKm()
# response = openkm.get_doc_by_folio('5293130')
# response = openkm.get_doc_by_folio('5293130')
response = openkm.download_doc('2b11d772-e2cb-4f5e-858f-7803624e22ff')

# print(response.content)
now = time.localtime(time.time())
fecha = time.strftime("%Y_%m_%d", now)
print(fecha)
with open("boleta_{}.pdf" .format(fecha), "wb") as pdf:
    pdf.write(response.content)
query = {
    'anio_doc':'2020'
}

