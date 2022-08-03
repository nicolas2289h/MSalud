#Nicolas Huanca - 2022
import fitz
import os
from timeit import default_timer

#------------------------------------ FUNCIONES ---------------------------------------

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
        salida.save(nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf', deflate=True)
        print('Archivo', 'generado: ' + nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf ✔ ✔')
    else:
        print('❌ NO SE PUDO GENERAR EL ARCHIVO', ' ' + nombre + ' ' + hospitales[posicion] + ' ' + codigoHospital[posicion] + '.pdf')
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


hospitales = ['Sequeiros R', 'Arroyabe R', 'Same_107 R', 'Centro Sanitario R', 'Pablo Soria R', 'Materno Infantil Dr Hector Quin R', 'San Roque R', 'Nuestra señora del carmen R', 'Dr Arturo Zabala R', 'Dr Guillermo Paterson R', 'Escolastico Zegada R', 'Dr Oscar Orias R', 'Hospital San Miguel R', 'Hospital Maimara R', 'Dr Salvador Mazza R', 'Gral Belgrano R', 'Ntra Sra Del Rosario R', 'Dr Jorge Uro R', 'Calilegua R', 'Ntra Sra Del Pilar R', 'Ntra Sra Del Valle R', 'Ntro Sr De La Buena Esperanza R', 'La Mendieta R', 'Wenceslao Gallardo R', 'Ing Carlos Snopek R', 'San Isidro Labrador R', 'Hospital Susques R']
codigoHospital = ['5-03', '5-04', '6-07', '6101', '6102', '6103', '6104', '6106', '6107', '6109', '6110', '6111', '6112', '6113', '6114', '6115', '6116', '6117', '6118', '6119', '6120', '6121', '6122', '6123', '6124', '6125', '6126']

x = [['NUM', 'CODIGO', 'HOSPITAL'], ['1', 'R 5-03', 'Sequeiros'], ['2', 'R 5-04', 'Arroyabe'], ['3', 'R 6-07', 'Same_107'], ['4', 'R 6101', 'Centro Sanitario'], ['5', 'R 6102', 'Pablo Soria'], ['6', 'R 6103', 'Materno Infantil Dr Hector Quin'], ['7', 'R 6104', 'San Roque'], ['8', 'R 6106', 'Nuestra señora del carmen'], ['9', 'R 6107', 'Dr Arturo Zabala'], ['10', 'R 6109', 'Dr Guillermo Paterson'], ['11', 'R 6110', 'Escolastico Zegada'], ['12', 'R 6111', 'Dr Oscar Orias'], ['13', 'R 6112', 'Hospital San Miguel'], ['14', 'R 6113', 'Hospital Maimara'], ['15', 'R 6114', 'Dr Salvador Mazza'], ['16', 'R 6115', 'Gral Belgrano'], ['17', 'R 6116', 'Ntra Sra Del Rosario'], ['18', 'R 6117', 'Dr Jorge Uro R'], ['19', 'R 6118', 'Calilegua R'], ['20', 'R 6119', 'Ntra Sra Del Pilar'], ['21', 'R 6120', 'Ntra Sra Del Valle'], ['22', 'R 6121', 'Ntro Sr De La Buena Esperanza'], ['23', 'R 6122', 'La Mendieta R'], ['24', 'R 6123', 'Wenceslao Gallardo'], ['25', 'R 6124', 'Ing Carlos Snopek'], ['26', 'R 6125', 'San Isidro Labrador'], ['27', 'R 6126', 'Hospital Susques'],]


print(' ')
for y in x:
    NUMERO, CODIGO, HOSPITAL = y
    print('{:<5} {:<10} {:<20}'.format(NUMERO, CODIGO, HOSPITAL))

while(True):
    opcion = input('\nElija el Numero de Hospital que desea extraer (1 - 27): ')
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion > 0 and opcion < 28:
            break
        else:
            print('OPCION NO VALIDA. DEBE ELEGIR UN NUMERO EN EL RANGO 1 - 27')
    else:
        print('OPCION NO VALIDA. DEBE ELEGIR UN NUMERO EN EL RANGO 1 - 27')

inicio = default_timer()
iniciarProceso(opcion - 1)
fin = default_timer()
tiempo = fin - inicio

if tiempo > 59:
    print('\nTiempo de ejecucion: ', round(tiempo/60, 2), ' minutos.')
else:
    print('\nTiempo de ejecucion: ', round(tiempo, 2), ' segundos.')
