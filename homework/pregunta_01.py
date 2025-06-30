# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    import zipfile
    import os
    import pandas as pd

    # 1. Descomprimir archivo zip
    ruta_zip = 'files/input.zip'
    carpeta_destino = 'input'

    # Solo descomprime si aún no existe la carpeta
    if not os.path.exists(carpeta_destino):
        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(carpeta_destino)

    # 2. Función para procesar los archivos y crear un DataFrame
    def crear_dataset(ruta_base):
        datos = []
        for sentimiento in ['positive', 'negative', 'neutral']:
            carpeta_sentimiento = os.path.join(ruta_base, sentimiento)
            for archivo in os.listdir(carpeta_sentimiento):
                ruta_archivo = os.path.join(carpeta_sentimiento, archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    frase = f.read().strip()
                    datos.append({
                        'phrase': frase,
                        'target': sentimiento
                    })
        return pd.DataFrame(datos)

    # 3. Crear los DataFrames
    df_train = crear_dataset('input/train')
    df_test = crear_dataset('input/test')

    # 4. Crear carpeta de salida si no existe
    os.makedirs('output', exist_ok=True)

    # 5. Guardar CSVs
    df_train.to_csv('output/train_dataset.csv', index=False)
    df_test.to_csv('output/test_dataset.csv', index=False)


    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
