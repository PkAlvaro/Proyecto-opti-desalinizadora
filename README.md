# Proyecto-opti-desalinizadora

Este repositorio contiene un conjunto de archivos que implementan un modelo de optimización para minimizar los costos operativos de una planta desalinizadora de agua de mar utilizando Gurobi-Python.

## Descripción del repositorio

El modelo de optimización se basa en una serie de variables y restricciones que representan el comportamiento de la planta y las limitaciones ambientales, de consumo eléctrico y ruido que se deben tomar en cuenta. El objetivo es minimizar los costos operativos totales, teniendo en cuenta los costos asociados con la energía, la maquinaria y el mantenimiento.

El repositorio incluye los siguientes archivos:

* `main.py`: este archivo contiene la implementación del modelo de optimización utilizando Gurobi-Python. Se definen las variables, restricciones y objetivo del modelo.
* `data.csv`: este archivo contiene los datos de entrada para el modelo de optimización, incluyendo los costos asociados con la energía, la maquinaria y el mantenimiento, así como la capacidad de producción de la planta y la demanda de agua.
* `output.csv`: este archivo contiene los resultados de la optimización, incluyendo la cantidad de agua producida, los costos totales y las variables de decisión.
* `README.md`: este archivo contiene información detallada sobre el repositorio, incluyendo una descripción del modelo de optimización y cómo ejecutar el código.

## Uso del repositorio

Para utilizar el modelo de optimización, se deben seguir los siguientes pasos:

1. Clonar el repositorio en una carpeta local.
2. Abrir `main.py` y configurar los parámetros de entrada según los requerimientos del usuario.
3. Ejecutar el archivo `main.py` para resolver el modelo de optimización.
4. Revisar los resultados en el archivo `output.csv`.

Este repositorio es útil para cualquier persona que esté interesada en optimizar los costos operativos de una planta desalinizadora de agua de mar utilizando Gurobi-Python. Los usuarios pueden ajustar los parámetros de entrada según sus necesidades y obtener los resultados de optimización correspondientes. Además, el código es fácilmente modificable para agregar nuevas restricciones o variables de decisión si es necesario.
