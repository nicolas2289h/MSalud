#Nicolas Huanca - 2022
import fitz
import os
from timeit import default_timer

def iniciarProceso(posicion):
    listaPaginas = []

    for pagina in documento:
        texto = pagina.get_text()
        encontrado = texto[0:95].find(codigoHospital[posicion])
        if encontrado != -1:
            listaPaginas.append(pagina)
            pass

    cadena = str(listaPaginas)
    paginas = [int(s) for s in cadena.split() if s.isdigit()]

    if bool(paginas):
        salida = fitz.open()
        for m in range(len(paginas)):
            salida.insert_pdf(documento, from_page=paginas[m], to_page=paginas[m])
        salida.save(nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf')
        print('✔ Archivo', (posicion + 1), 'generado: ' + nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf')
    else:
        print('❌ NO SE PUDO GENERAR EL ARCHIVO', (posicion + 1), ' ' + nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf')
    return


#------------------------------------ PRINCIPAL ---------------------------------------

while(True):
    nombre = input('\nCopiar y pegar aqui el nombre del archivo PDF (sin la extension): ')
    if os.path.isfile(nombre+'.pdf'):
        pdfFile = nombre + '.pdf'
        break
    else:
        print('No se encontró el archivo. Recuerde que el nombre no debe incluir la extension \".pdf\"')


documento = fitz.open(pdfFile)

# listas de hospitales con sus respectivos codigos
hospitales = ['Sequeiros R', 'Arroyabe R', 'Same_107 R', 'Centro Sanitario R', 'Pablo Soria R', 'Materno Infantil Dr Hector Quin R', 'San Roque R', 'Nuestra señora del carmen R', 'Dr Arturo Zabala R', 'Dr Guillermo Paterson R', 'Escolastico Zegada R', 'Dr Oscar Orias R', 'Hospital San Miguel R', 'Hospital Maimara R', 'Dr Salvador Mazza R', 'Gral Belgrano R', 'Ntra Sra Del Rosario R', 'Dr Jorge Uro R', 'Calilegua R', 'Ntra Sra Del Pilar R', 'Ntra Sra Del Valle R', 'Ntro Sr De La Buena Esperanza R', 'La Mendieta R', 'Wenceslao Gallardo R', 'Ing Carlos Snopek R', 'San Isidro Labrador R', 'Hospital Susques R']
codigoHospital = ['5-03', '5-04', '6-07', '6101', '6102', '6103', '6104', '6106', '6107', '6109', '6110', '6111', '6112', '6113', '6114', '6115', '6116', '6117', '6118', '6119', '6120', '6121', '6122', '6123', '6124', '6125', '6126']

inicio = default_timer()
for i in codigoHospital:
    iniciarProceso(codigoHospital.index(i))
fin = default_timer()
tiempo = fin - inicio

if tiempo > 59:
    print('\nTiempo de ejecucion: ', round(tiempo/60, 2), ' minutos.')
else:
    print('\nTiempo de ejecucion: ', round(tiempo, 2), ' segundos.')