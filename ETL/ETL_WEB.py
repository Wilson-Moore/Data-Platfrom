import requests
from dotenv import dotenv_values
from bs4 import BeautifulSoup


ENV_KEYS=dotenv_values(".env")

res=requests.get(ENV_KEYS.get("WEBSITE"))

soup=BeautifulSoup(res.content,"html.parser")
print(soup.prettify)