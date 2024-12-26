from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path
from modules.config import RAW_DATASETS, PROCESSED_DATASETS, KAGGLE_DATASET_URL, ENV_FILE_PATH

# load emviroment variables from .env file
load_dotenv(ENV_FILE_PATH)

def web_scraping_from_kaggle_api():

    # set kaggle enviorment variables with enviroment variables declare into .env file
    os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
    os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

    # kaggle client initialize and api autenticate
    api = KaggleApi()
    api.authenticate() 

    # declare and check if existe output directory of big-five dataset and .csv into this folder
    list_directorios = Path(RAW_DATASETS)
    list_csv = list(list_directorios.glob('*csv'))

    if len(list_csv) > 0:
        # download .csv from kaggle using api
        api.dataset_download_files(KAGGLE_DATASET_URL, path=RAW_DATASETS, unzip=True)
        print(f"Dataset descargado y descomprimido en {RAW_DATASETS}")
    else:
        print(f"Dataset ya fue descargado y descomprimido en {RAW_DATASETS}")

