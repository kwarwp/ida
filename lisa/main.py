# ida.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 
HOMEM_ARANHA = "http://pngimg.com/uploads/spider_man/spider_man_PNG53.png"
FLORESTA = "https://pre00.deviantart.net/e7ab/th/pre/f/2016/173/6/7/forest_clearing_background_png_stock_0075__2__copy_by_annamae22-da5zx2y.png"
CIDADE = "https://s2.glbimg.com/1Wh9VrSZokI1CoRhHpdgeTapEnI=/e.glbimg.com/og/ed/f/original/2018/02/22/cidade.jpg"
TARZAN = "https://therottingbat.files.wordpress.com/2014/01/tarzan_1999.jpg"
BARBIE = "https://image.afcdn.com/story/20151130/-820959_w767h767c1cx510cy248.jpg"
CANO = "https://thumbs.dreamstime.com/b/homem-no-t%C3%BAnel-com-oceano-sombrio-85554705.jpg"
APARTAMENTO = "https://odis.homeaway.com/odis/listing/62148fe8-8822-45ed-830f-5f36b72cc271.c10.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    
    floresta.direita = cidade
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="homem_aranha", style=dict(left=150, top=150, width=60, height=200)
    homem_aranha.entra(floresta)
    ehomem_aranha = Texto(floresta, "eu sabia que não devia ter bebido outra taça de vinho"
    homem_aranha.vai=falahomem_aranha.vai
    etarzan = Texto(apartamento, "minha primeira festa na cidade e eu acordo no apartamento de um desconhecido!"
    tarzan.vai=falatarzan.vai
    ehomem_aranha = Texto(cidade, "ainda bem que havia um tunel para a cidade"
    homem_aranha.vai=falahomem_aranha.vai
    #tarzan = Elemento(img=TARZAN, tit="tarzan", style=dict(left=150, top=150, width=60, height=200)
    #barbie = Elemento(img=BARBIE, tit="barbie", style=dict(left=150, top=150, width=60, height=200)