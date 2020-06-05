from application.model.entity.comentario import Comentario
from flask import current_app

class ComentarioDAO():
    def __init__(self):
        self._comentarios= []
        self.ids_gerados = 1
    
    def getComentarios(self):
        return self._comentarios
    
    def addComentario(self, comentario):
        self._comentarios.append(comentario)

    def encontrarComentarioPorVideoId(self, id_video):
        comentarios = current_app.config['comentarios']
        comentarios_video = []
        for i, comentario in enumerate(comentarios.getComentarios()):
            if comentario.getVideoId() == id_video:
                comentarios_video.append(comentario)
        return comentarios_video
    
    def deletarComentarioPorId(self,id_comentario):
        comentarios = current_app.config['comentarios']
        for i, comentario in enumerate(comentarios.get_comentarios()):
            print(comentarios.get_comentarios())
            print(comentario.get_id(),id_comentario)
            if comentario.get_id() == id_comentario:
                self._comentarios.pop(i)
                return comentario
        return None