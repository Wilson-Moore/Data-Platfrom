from typing import Dict
from .transform_images import transform_ocr
from .transform_database import transform_erp
def transfrom(ENV_KEYS:Dict[str,str|None]) -> None:
    print("TRANSFROMING IMAGES")
    transform_ocr(ENV_KEYS.get("IMAGES_PATH"))
    print("DONE TRANSFROMING IMAGES")
    print("TRANSFROMING ERP")
    transform_erp()
    print("DONE TRANSFROMING ERP")