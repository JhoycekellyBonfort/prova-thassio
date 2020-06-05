import random
class Video:
    def __init__(self,id, titulo, descricao, thumb, src, id_categoria, publicacao):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._thumb = thumb
        self._src = src
        self._id_categoria = id_categoria
        self._publicacao = publicacao
        self._curtidas =  random.randint(0,100)
        self._visualizacoes =  random.randint(100,10000)
    
    def getId(self):
        return self._id

    def getIdCategoria(self):
        return self._id_categoria

    def getCurtidas (self):
        return self._curtidas

    def getVisualizacoes (self):
        return self._visualizacoes

    def getTitulo (self):
        return self._titulo
    
    def getDescricao (self):
        return self._descricao

    def getThumb (self):
        return self._thumb

    def getSrc (self):
        return self._src

    def getPublicacao (self):
        return self._publicacao
    
    def setVisualizacoes(self,visualizacoes):
        self._visualizacoes = visualizacoes
    
    def setCurtidas(self,curtidas):
        self._curtidas = curtidas