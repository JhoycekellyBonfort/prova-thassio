from flask import Flask, session
import os
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.comentarioDAO import ComentarioDAO


app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"),
)
categorias   = CategoriaDAO ()
videos       = VideoDAO ()
comentarios     = ComentarioDAO ()
app.config['categorias'] = categorias
app.config['videos']     = videos
app.config['comentarios']     = comentarios

from application.controller import inicioController
from application.controller import categoriaController
from application.controller import videoController
