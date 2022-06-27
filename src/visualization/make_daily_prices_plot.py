
def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    >>> make_daily_prices_plot()
    """
    
    import pandas as pd
    import matplotlib.pyplot as plt
    path_file = r'data_lake/business/precios-diarios.csv'
    datos = pd.read_csv(path_file, index_col=None, sep=',', header=0)
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    x = datos.Fecha
    y = datos.Precio

    plt.figure(figsize=(15, 6))
    plt.plot(x, y, 'b', label='Promedio Diario')
    plt.title('Promedio Diario')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig("data_lake/business/reports/figures/daily_prices.png")



if __name__ == "__main__":
    import doctest

    doctest.testmod()
