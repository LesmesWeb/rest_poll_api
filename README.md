# Polls API Rest

Este proyecto esta basado en el libro **Building APIs with Django and Django Rest Framework Release 2.0**  en el que se están implementando reglas y conocimientos que he adquirido.

## Capitulo 1 y 2

- Configuración inicial del proyecto:
-- Declaración de modelos.
-- Url app ***polls***.
-- Configuración del administrador.

## Capitulo 3

En este capítulo, se creara una API con Django puro. No se utilizara Django Rest Framework (ni ninguna otra biblioteca).

Desde postman por get se mostrarala de la siguiente manera:

```sh
http://localhost:8000/polls/

{
    "results": [
        {
            "question": "¿Te gustaria aprender JavaScript?",
            "created_by__username": "admin",
            "pub_date": "2020-04-06T17:11:00.312Z"
        },
        {
            "question": "¿Cuál es tu nivel con JavaScript?",
            "created_by__username": "Camilo",
            "pub_date": "2020-04-06T17:15:37.472Z"
        }
    ]
}

http://localhost:8000/polls/1/

{
    "results": {
        "question": "¿Te gustaria aprender JavaScript?",
        "created_by": "admin",
        "pub_date": "2020-04-06T17:11:00.312Z"
    }
}
```

**¿Por qué necesitamos DRF (DRF = Django Rest Framework) ?**

Pudimos construir la API solo con Django, sin usar DRF, entonces, ¿por qué necesitamos DRF? Casi siempre necesitará tareas comunes con sus API, como control de acceso, serialización, limitación de velocidad y más.
DRF proporciona un conjunto bien pensado de componentes básicos y puntos de conexión convenientes para construir API. 
 