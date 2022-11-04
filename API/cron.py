#de ser necesario se podria importar la libreria loggin para consultar y mostrar el registro de la operacion
#este procesimiento "log" lo piden en los requerimientos y es necesario ver si se aplica 

#importamos la clase completa openKM para crear una instancia en cron

import time
from django.http import HttpResponse
from API.openKM import OpenKm

#a manera de prueba sabremos si esta funcionando crontab "preguntando" con parametro "request".

def opkm(request): 
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
        'anio_doc':'2020'}
    return HttpResponse("función cron openkm funcionnando")