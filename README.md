# Proyecto: Gestión de Cambios (ADSI'R)

El proyecto de gestión de cambios se basa en un proyecto de simulación para la práctica de programación, investigación, aplicación de la lógica, aplicación/llenado de formatos, análisis de requisitos, aplicación de SCRUM, cambio de roles y gestión de proyectos. El ejercicio fue propuesto por el instructor HHHH el cuál se autodenominó empresa "Las cuatro mudas" y tomó el rol de contratante, asignando este proyecto denominado "ADSI 'Responsables'" con el rol de contratistas.

## Índice

1. Manual de configuración
	- Pre-requisitos
		- Consola en windows
		- Ubicación de carpeta específica
	- Instalación
	

## [Manual de configuración](#manual)

Mediante el siguiente manual, se explicara sobre como poder ejecutar el proyecto o repositorio para poder trabajar en su ordenador. De esta forma se garantiza el correcto funcionamiento del programa en una computadora local.

### Pre-requisitos

Comenzado, este manual está específicado únicamente para la plataforma de Windows, en caso de querer seguir este proceso para otro sistema operativo, deberá consultar los comandos usted mismo. Para clonar el repositorio en tu local, vas a  necesitar las siguientes dependencias/librerias o software instalado:

- [Git](https://git-scm.com/download/win)
- [Python](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- [pandas](https://pandas.pydata.org/getting_started.html)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/#installation)
- [numpy](https://numpy.org/install/)
- [xlrd](https://pypi.org/project/xlrd/)
- [fsspec](https://filesystem-spec.readthedocs.io/en/latest/#installation)

Para poder ejecutar y arrancar el programa en su local, necesitará usar la consola de comandos y/o terminal de preferencia `Bash`, `Powershell` o `cmd`

#### Para abrir una consola en Windows:

Utilizamos las teclas `WIN + R` y escribimos el ejecutable de nuestra terminal/consola, para este ejemplo se utilizará [Powershell](https://docs.microsoft.com/en-us/powershell/). A continuación se indica como:

![Ejecutar terminal](https://i.imgur.com/f7F0XZS.png)

#### Ubicarse en una carpeta de su ordenador:

Para clonar el repositorio en una carpeta específica, deberá usar el comando `cd nombrecarpeta`. Para este ejemplo, nos ubicaremos en el escritorio:

![Ubicación del escritorio](https://i.imgur.com/MipqZz3.png)

Con los pasos anteriormente dados, estará listo para usar una consola de comandos y clonar correctamente el repositorio en su local. En el siguiente topic se le indicará como instalar correctamente el programa.


### Instalación

A continuación se darán una serie de pasos los cuales indicarán como se puede instalar el proyecto o repositorio en su local (ordenador propio).

1. Paso: Copiar la URL (protocolo HTTP) para clonar el repositorio.

```
	https://github.com/briancastro-bc/adsi-responsables.git
```

2. Paso: Abrir una terminal y ejecutar el siguiente comando (en los Pre-requisitos se explica como abrir una terminal en Windows).

```
	git clone https://github.com/briancastro-bc/adsi-responsables.git
```
3. Paso: Ir a carpeta del repositorio clonado:

```
	cd adsi-responsables
```

4. Paso: Actualizar el gestor de paquetes (pip):

```
	pip install --upgrade pip
```

5. Paso: Instalar los paquetes necesarios para arrancar el programa:

```
	pip install pandas openpyxl numpy xlrd fsspec
```

6. Paso: Ejecutar el archivo/módulo de arranque:

```
	py main.py
```
