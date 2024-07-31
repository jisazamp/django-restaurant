# Ejercicio (parte 1)

1. Clonar este repositorio
2. Dentro de la carpeta del proyecto anterior que clonó, cree un nuevo ambiente virtual ejecutando el siguiente comando `python -m venv env`. Si está desde Linux o macOS, use el siguiente comando: `python3 -m venv env`
3. Active el entorno virtual usando el siguiente comando `./env/Scripts/activate`. Si está desde Linux o macOS, use el siguiente comando: `source ./env/bin/activate`
4. Agregue un card (dentro del template de `menu.html`) que muestre los detalles de un producto del restaurante usando Bootstrap: [https://getbootstrap.com/docs/5.2/components/card/]()
5. Hecha la card, pase como contexto en la vista (`menu/views.py`), un listado de productos para listarlos de manera dinámica en la vista, así:
   
   ```
   def menu(request):
    productos = [
        {
            "id": 1,
            "title": "Burger",
            "description": "Lorem ipsum dolor amet",
            "price": 38000,
        },
    ]

    return render(request, "menu.html", {"productos": productos})
   ```
6. Por último, usando un ciclo for en la plantilla de `menu.html`, renderice todos los productos pasados desde el contexto anterior. La sintaxis para hacer un ciclo for desde una plantilla es la siguiente:

```
{% for producto in productos %}
<div class="card">
  ...
</div>
{% endfor %}
```

# Ejercicio (parte 2)

1. Consulte la documentación de Leaflet: [https://leafletjs.com/examples/quick-start/]()
2. Instale Leaflet en el proyecto (son los dos primeros pasos de la documentación del punto anterior)
3. Cree una nueva plantilla (dentro de la carpeta de templates) para mostrar el mapa
4. Cree una nueva ruta (`urls.py`) para renderizar esta nueva ruta.
