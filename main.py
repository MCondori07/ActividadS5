import pandas as pd

def cargar_datos(ruta):
    """Función inicial para leer el dataset del e-shop 2008."""
    return pd.read_csv(ruta, sep=';')


if __name__ == "__main__":
    df = cargar_datos("e-shop clothing 2008.csv")
    print(df.head())