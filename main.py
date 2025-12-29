from ETL.Extract import extract
from ETL.Transform import transfrom
from dotenv import dotenv_values

ENV_KEYS=dotenv_values(".env")

extract(ENV_KEYS)

transfrom(ENV_KEYS)