'''
# se crea una lista por cada carpeta raíz de la estructura
# creación carpeta data_lake
# creación de cada carpeta dentro de data_lake


'''
def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```

    >>> create_data_lake()
    """
    import os 
    data_lake = [
        "landing",
        "raw",
        "cleansed",
        "business",
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]

    
    os.mkdir("data_lake")

    
    for folder in data_lake:
        os.mkdir(os.path.join("data_lake", folder))

    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    import doctest
    
    doctest.testmod()
    