from flask import current_app

class Categoria:

    def __init__(self, id, nome, descricao,imagem):
        self._id = id
        self._nome = nome 
        self._descricao = descricao
        self._imagem = imagem

    def getDescricao (self):
        return self._descricao

    def getImagem (self):
        return self._imagem

    def getNome (self):
        return self._nome

    def setId (self, id):
        self._id = id

    def getId (self):
        return self._id
    
    def getVideosPorCategoriaId(self):
        videos = current_app.config['videos']
        videos_na_categoria = []
        for index, item in enumerate(videos.getVideos()):
            if item.getIdCategoria() == self.getId():
                videos_na_categoria.append(item)
        return videos_na_categoria