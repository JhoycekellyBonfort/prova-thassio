from application.model.entity.video import Video
from flask import current_app

class VideoDAO:
    
    def __init__(self):
        self._videos = []
        self._videos.append(Video(1, "COMPRINHAS NO SITE DE MAQUIAGEM MAIS BARATO 😱🔥", "Olá meus amores, nesse vídeo eu realizei uma compra de maquiagem no site mais barato da internet, SIM, O MAIS BARATO, e mostrei tudinho pra vocês, vem ver comigo os produtos, preço, reações, e se vale a pena.. espero que gostem, beijão! ", "/videos/thumbs/comprinhas.png",'videos/comprinhas.mp4',1,"11/10/2010"))
        self._videos.append(Video(2, "Secretário da saúde de Osasco sofre ataque", "Secretário da saúde de Osasco sofre ataque.", "/videos/thumbs/saude.png","videos/saude.mp4",2,"15/08/2020"))
        self._videos.append(Video(3, "Comprinhas de MAKE pela Internet", "Descobri um site super confiável para comprar as mesmas maquiagens que vendem na 25 de março e com o mesmo preço! Se você ama colecionar make ou é iniciante na maquiagem e quer comprar suas makes sem gastar muito, você vai amar essa dica!", "/videos/thumbs/make.png","videos/make.mp4",1,"04/10/2018"))
        self._videos.append(Video(4, "As principais notícias do Rio de Janeiro nesta quinta-feira ", "As principais notícias do Rio de Janeiro nesta quinta-feira", "/videos/thumbs/rio.png","videos/rio.mp4",2, "05/07/2019"))
       
    def getVideoPorId(self, id):
        video = None
        for index, item in enumerate(self.getVideos()):
            if item.getId() == id:
                video = item
                return video
        return video

    def getVideos(self):
        return self._videos

    def getVideosMaisCurtidos(self):
        videos = current_app.config['videos']
        mais_curtidos = sorted(videos.getVideos(), key=lambda x: x.getCurtidas(), reverse=True)
        return mais_curtidos