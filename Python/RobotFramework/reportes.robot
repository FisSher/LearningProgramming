*** Settings ***
Documentation     Extracción de los reportes del sitio #(Censurado por motivos de privacidad y seguridad)  #Simplemente info
Library           SeleniumLibrary  10s  #10 segundos para esperar cualquier cosa de la librería

*** Variables ***
${SavePath}     #Acá vamos a guardar todos los reportes
${SPO}      #(Censurado por motivos de privacidad y seguridad)  #El link tiene las credenciales de login, sino da error
${BROWSER}        Chrome  #Esto requiere chromedriver sino no abre ningún navegador
${Proyecto}       #(Censurado por motivos de privacidad y seguridad)  #SIN ESTO NO HAY COOKIE

#Links de los sitios
#(Censurado por motivos de privacidad y seguridad)
#Fin links de los sitios

#Botones
${AbreFases}  id:Phases_span  #Boton para ir a elegir fases
${AceptaFase}  class:ui-dialog-buttonset  #Boton para aceptar las fases seleccionadas
${EjecutarReporte}  id:btnExecute  #Botón Procesar
${StatusReporte}  reportStatus  #Cuando aparece el mensaje listo
${DescargaReporte}  class:getReportLink  #Link para bajar el reporte
${CheckboxDetallado}  id:selByParent_-1  #Este checkbox es el que agrega el detalle completo
${MensajeReporteListo}  Reporte listo.  #Se guía por este mensaje para empezar la descarga
${DolarAmericano}  166  #Indice de Dolar americano
${MonedaPresDetallado}  id:Currency  #Listado de moneda


*** Test Cases ***
Selección proyecto
    Open Browser    ${SPO}    ${BROWSER}  #Seteo de cookie para los proyectos
    Maximize Browser Window
    Title Should Be    SPO - Sistema de Presupuestación de Obras  #Me aseguro que estoy en la Home
    Wait Until Element Is Visible  ${Proyecto}
    Double Click Element   ${Proyecto}
    Sleep  3s  #Le doy un tiempo de espera para asegurar la cookie
#Ahora se pueden ejecutar la descarga de todos los reportes

Descarga Reporte 054
    Go To  ${Reporte054}
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  30s  #Espera los checkbox
    Click Element  ${CheckboxDetallado}  #Selecciona el checkbox con mas detalles
    Click Element  ${AceptaFase}  #click en aceptar
    Click Element  ${EjecutarReporte}  #Click en ejecutar el proceso
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s  #Espera hasta que aparezca el boton descargar
    Click Element  ${DescargaReporte}  #Click en descargar
    Sleep  10s  #Esperamos la descarga
#Fin Reporte 054

Descarga Edicion Masiva Recursos
    Go To  ${EdicionMasiva}
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  60s  #Esperamos el botón
    Click Element  ${CheckboxDetallado}  #Selecciona el checkbox con mas detalles
    Click Element  ${AceptaFase}  #click en aceptar
    Click Element  ${EjecutarReporte}  #Click en ejecutar el proceso
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s  #Espera hasta que aparezca el boton descargar tomando referencia lo que dice el HTML
    Click Element  ${DescargaReporte}  #Click en descargar
    Sleep  10s  #Esperamos la descarga
#Fin Edicion Masiva

Descarga Por Fase
    Go To  ${PorFase}
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  60s  #Espero el checkbox
    Click Element  ${CheckboxDetallado}  #Selecciono
    Click Element  ${AceptaFase}  #Boton aceptar
    Click Element  ${EjecutarReporte}  #Botón de generar
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s
    Click Element  ${DescargaReporte}  #Click en descargar
    Sleep  10s  #Esperamos la descarga
#Fin Por Fase

Descarga Histograma de Equipos
    Go To  ${HistogramaEquipos}
    Wait Until Element Is Visible  ${AbreFases}  30s
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  40s
    Click Element  ${CheckboxDetallado}
    Click Element  ${AceptaFase}
    Click Element  ${EjecutarReporte}
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s  #Espera hasta que aparezca el boton descargar tomando referencia lo que dice el HTML
    Click Element  ${DescargaReporte}  #Click en descargar
    Sleep  10s  #Esperamos la descarga
#Fin Histograma de Equipos

Descarga Histograma de Personal
    Go To  ${HistogramaPersonal}
    Wait Until Element Is Visible  ${AbreFases}  30s
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  40s
    Click Element  ${CheckboxDetallado}
    Click Element  ${AceptaFase}
    Click Element  ${EjecutarReporte}
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s
    Click Element  ${DescargaReporte}
    Sleep  10s
#Fin Histograma de Personal


Descarga Bajada Plana
    Go To  ${BajadaPlana}
    Wait Until Element Is Visible  ${EjecutarReporte}  10s
    Click Element  ${EjecutarReporte}
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s
    Click Element  ${DescargaReporte}
    Sleep  10s
#Fin Bajada Plana


Descarga Analisis Precios por Fase
    Go To  ${AnalisisPorFase}
    Wait Until Element Is Visible  ${AbreFases}  30s
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  40s
    Click Element  ${CheckboxDetallado}
    Click Element  ${AceptaFase}
    Wait Until Element Is Visible  ${EjecutarReporte}  10s
    Click Element  ${EjecutarReporte}
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  480s
    Click Element  ${DescargaReporte}
    Sleep  10s
#Fin Analisis por fase

Descarga Presupuesto Detallado
    Go To  ${PresupuestoDetallado}
    Wait Until Element Is Visible  ${AbreFases}  30s
    Click Element  ${AbreFases}
    Wait Until Element Is Visible  ${CheckboxDetallado}  40s
    Click Element  ${CheckboxDetallado}
    Click Element  ${AceptaFase}
    Select From List By Value  ${MonedaPresDetallado}  ${DolarAmericano}  #Hay que seleccionar moneda
    Click Element  ${EjecutarReporte}
    Wait Until Element Contains  ${StatusReporte}  ${MensajeReporteListo}  360s
    Click Element  ${DescargaReporte}
    Sleep  10s
#Fin Presupuesto Detallado
    [teardown]  Close Browser  #En el último caso dejar el teardown así se cierra el navegador