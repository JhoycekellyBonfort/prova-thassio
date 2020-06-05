from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from flask import current_app
import logging

class CategoriaDAO():
    def __init__(self):
        
        self._categorias= []
        self._categorias.append(Categoria(1, "Maquiagem", "Assista videos sobre maquiagem","/categorias/maquiagem.jpg"))
        self._categorias.append(Categoria(2, "Noticias", "Assista as ultimas noticias","/categorias/noticias.png"))
        self._categorias.append(Categoria(3, "jogos", "Assista videos de jogos","/categorias/jogos.png"))
    
    def getCategorias(self):
        return self._categorias

    def getCategoriaPorId(self, id):
        categoria = None
        for index, item in enumerate(self.getCategorias()):
            if item.getId() == id:
                categoria = item
                return categoria
        return categoria
