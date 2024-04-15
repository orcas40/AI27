# AI27
technical test

***
## Description
***
Objetivo:
Demostrar habilidades en la automatización de tareas de extracción de datos web y generación de archivos Excel mediante Python y Selenium.
Descripción de la tarea:
El candidato deberá crear un script automatizado con las siguientes acciones:

1. Creación de Cuenta y Login en Wikipedia:
    - Automatizar la creación de una cuenta en Wikipedia (Opcional, pero con valor adicional).
    - Loguearse en Wikipedia con la cuenta creada.

2. Extracción de Información de Entidades Federativas de México:
    - Navegar a la página "Entidades federativas de México" en Wikipedia.
    - Extraer la siguiente información:
        a) Información de la tabla de Entidades federativas de México por superficie, población y densidad.
        b) Información de la tabla de Población histórica de México de Censos.
        c) Información de la tabla de Población histórica de México de Proyecciones de población.
            i) Para cada estado en la lista, navegar a su página específica y extraer la sección de "Toponimia".

3. Extracción de Información de Estados de los Estados Unidos:
    - Navegar a la página "Estado de los Estados Unidos" en Wikipedia.
    - Extraer la siguiente información:
        a) Listado de Estados.
            i) Para cada estado en la lista, navegar a su página específica y extraer la sección de "Etimología".

4. Generación de Archivos Excel:
    - Crear un archivo Excel para cada extracción anterior realizada tanto para México (a, b y c) como para Estados Unidos (a). Cada archivo debe tener un nombre descriptivo y la información debe estar organizada de manera clara

***
## Installation
***
Pasos para instalar.
Nota: este script se ejecuta en python 3.11 para ello se debe tener instalado esta version para no tener problemas
```

$ git clone https://github.com/orcas40/AI27.git
$ cd AI27
$ pip3 install selenium
$ pip3 install xlsxwriter
```
***
## Ejecucion
***
Pasos para ejecutar el script.
```
$ python3 procesar.py
```
***
## Salidas
***
Se generaran dos archivos xlsx. en el directorio Raiz (AI27)
DataWikipedia_mexico.xlsx
DataWikipedia_usa.xlsx



