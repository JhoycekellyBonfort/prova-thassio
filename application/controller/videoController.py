from application import app
import json
from flask import render_template, request, jsonify, current_app,Response
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.comentarioDAO import ComentarioDAO
from application.model.entity.comentario import Comentario



@app.route("/video/buscar")
def buscar():
    try:
        texto_buscado = request.args.get('texto').lower()
        videos = current_app.config['videos']
        busca = [x.__dict__ for x in videos.getVideos() if  texto_buscado in x.getTitulo().lower() ]
        return Response(json.dumps(busca),  mimetype='application/json') 
    except Exception as e:
        return str(e)

@app.route("/video/curtir")
def like():
    try:
        videos = current_app.config['videos']           
        id_video = int(request.args.get('id_video'))     
        video = videos.getVideoPorId(id_video)         
        curtidas = (video.getCurtidas()) + 1         
        video.setCurtidas(curtidas)                  
        return jsonify(curtidas = curtidas)
    except Exception as e:
        return str(e)

@app.route("/video/comentario")
def comentario():
    try:
        comentarios = current_app.config['comentarios']                                                                    
        comentarios.ids_gerados +=1                                                                                  
        comentario = Comentario(comentarios.ids_gerados,request.args.get('comentario'),int(request.args.get('id_video')))     
        comentarios.addComentario(comentario)                                                                                
        response = {'id':comentario.getId(), 'text':comentario.getTexto(), 'video_id': comentario.getVideoId()} 
        return jsonify(response)
    except Exception as e:
        return str(e)



@app.route("/categoria/<int:id_categoria>/video/<int:id_video>")
def video(id_categoria,id_video):
    videos = current_app.config['videos']
    categorias = current_app.config['categorias']
    comentarios = current_app.config['comentarios']
    categoria = categorias.getCategoriaPorId(id_categoria)
    videos_na_categoria = categoria.getVideosPorCategoriaId()
    video = videos.getVideoPorId(id_video)
    video.setVisualizacoes(video.getVisualizacoes() + 1)
    comentarios_video = comentarios.encontrarComentarioPorVideoId(video.getId())
    return render_template("video.html", video = video,categoria=categoria, comentarios = comentarios_video, lista_de_categorias = categorias.getCategorias())

