

class Comentario():

    def __init__(self,id,texto, video_id):
        self._texto = texto
        self._video_id = video_id
        self._id = id

    def getTexto(self):
        return self._texto

    def getId(self):
        return self._id

    def setTexto(self, text):
        self._texto = texto
    
    def getVideoId(self):
        return self._video_id