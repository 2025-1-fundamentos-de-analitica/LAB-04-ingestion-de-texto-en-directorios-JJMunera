# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.

"""

import zipfile
import os
import pandas as pd

def pregunta_01():
    """
    Genera los archivos train_dataset.csv y test_dataset.csv
    a partir de los archivos de texto descomprimidos.
    """
    # Define the base directory for input and output
    base_dir = "files"

    # Descomprimir el archivo input.zip
    # Ensure extraction happens into the 'files' directory
    with zipfile.ZipFile(os.path.join(base_dir, "input.zip"), "r") as zip_ref:
        zip_ref.extractall(base_dir) # Extract into 'files' directory

    # Crear la carpeta de salida si no existe
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Listas para almacenar los datos
    train_data = []
    test_data = []

    # Define the input base path
    input_base_path = os.path.join(base_dir, "input")

    # Recorrer la estructura de carpetas para train
    for sentiment in ["negative", "positive", "neutral"]:
        train_path = os.path.join(input_base_path, "train", sentiment)
        for filename in os.listdir(train_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(train_path, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()
                train_data.append({"phrase": phrase, "target": sentiment})

    # Recorrer la estructura de carpetas para test
    for sentiment in ["negative", "positive", "neutral"]:
        test_path = os.path.join(input_base_path, "test", sentiment)
        for filename in os.listdir(test_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(test_path, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()
                test_data.append({"phrase": phrase, "target": sentiment})

    # Crear DataFrames de pandas
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    # Guardar los DataFrames como archivos CSV en la carpeta de salida
    train_df.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)
    test_df.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)   



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
