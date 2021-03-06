

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.
    >>> make_monthly_prices_plot()
    """

    import pandas as pd
    import os

    # Importar el archivo de precios diarios
    os.chdir("./")
    
    grafica = pd.read_csv("data_lake/business/precios-mensuales.csv")
    # Guardar el grafico en formato PNG
    figura = grafica.plot(
        kind="line",
        x="Fecha",
        y="Precio",
        title="Precio Promedio Histórico Mensual",
        grid=True,
        figsize=(10, 5),
    ).get_figure()

    figura.savefig("data_lake/business/reports/figures/monthly_prices.png")


if __name__ == "__main__":
    import doctest

    doctest.testmod()