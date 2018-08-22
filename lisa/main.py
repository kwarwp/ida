# ida.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv 
HOMEM_ARANHA = "http://pngimg.com/uploads/spider_man/spider_man_PNG53.png"
FLORESTA = "https://pre00.deviantart.net/e7ab/th/pre/f/2016/173/6/7/forest_clearing_background_png_stock_0075__2__copy_by_annamae22-da5zx2y.png"
CIDADE = "https://s2.glbimg.com/1Wh9VrSZokI1CoRhHpdgeTapEnI=/e.glbimg.com/og/ed/f/original/2018/02/22/cidade.jpg"
TARZAN = "https://img00.deviantart.net/3c68/i/2011/322/7/f/tarzan_by_cassidy_morgan-d4gje1g.png"
BARBIE = "https://i.pinimg.com/originals/c8/10/fd/c810fdcf20e40ada63d977df77d25d29.png"
CANO = "https://thumbs.dreamstime.com/b/homem-no-t%C3%BAnel-com-oceano-sombrio-85554705.jpg"
APARTAMENTO = "https://odis.homeaway.com/odis/listing/62148fe8-8822-45ed-830f-5f36b72cc271.c10.jpg"
STYLE["width"] = 700
STYLE["height"] = "650px"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    cidade2 = Cena(img=CIDADE)
    cidade3 = Cena(img=CIDADE)
    apartamento = Cena(img=APARTAMENTO)
    
    floresta.direita = apartamento
    apartamento.esquerda = floresta
    apartamento.direita = cidade
    cidade.esquerda = apartamento
    cidade.direita = cidade2
    cidade2.esquerda = cidade
    cidade2.direita = cidade3
    cidade3.esquerda = cidade2
    
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="homem_aranha", style=dict(left=150, top=150))
    homem_aranha.entra(floresta)
    falahomem_aranha = Texto(floresta, "eu sabia que não devia ter bebido outra taça de vinho")
    homem_aranha.vai=falahomem_aranha.vai
    
    tarzan = Elemento(img=TARZAN, tit="tarzan", style=dict(left=150, top=150))
    tarzan.entra(apartamento)
    falatarzan = Texto(apartamento, "minha primeira festa na cidade e eu acordo no apartamento de um desconhecido!")
    tarzan.vai=falatarzan.vai
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="homem_aranha", style=dict(left=150, top=150))
    homem_aranha.entra(cidade)
    falahomem_aranha = Texto(cidade, "ainda bem que havia um tunel para a cidade")
    homem_aranha.vai=falahomem_aranha.vai
    
    homem_aranha = Elemento(img=HOMEM_ARANHA, tit="homem_aranha", style=dict(left=150, top=150))
    homem_aranha.entra(cidade2)
    falahomem_aranha = Texto(cidade2, "nossa! Que boneca!")
    homem_aranha.vai=falahomem_aranha.vai
    
    barbie = Elemento(img=BARBIE, tit="barbie", style=dict(left=150, top=150))
    barbie.entra(cidade3)
    falabarbie = Texto(cidade3, "sai fora aracnedeo!")
    barbie.vai=falabarbie.vai
    
    floresta.vai()
criarcenas()