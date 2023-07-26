import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


class Endpoints():
    def __init__(self, admin:bool=True) -> None:
        self._url = os.getenv('URL_ENDPOINTS')
        self._tipo_usuario = 'admin' if admin == True else 'user'

    @property
    def url(self):
        return self._url

    @property
    def usuario(self):
        return self._tipo_usuario

    def buscar_todos_quartos(self):
        url = self.url + f'/{self.usuario}/buscar-todos-quartos'
        quartos = requests.get(url)

        if quartos.status_code not in [200, 201]:
            return False

        quartos = json.loads(quartos.text)
        return quartos

# x = Endpoints().buscar_todos_quartos()
# print(x)