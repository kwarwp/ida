# ida.stacy.main.py
from _spy.vitollino.main import Cena, Elemento,Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 900

TARZAN = "https://vignette.wikia.nocookie.net/disney/images/6/6a/Tarzan_KH.png/revision/latest?cb=20130130213033"
ALICE = "https://i.pinimg.com/originals/53/dc/44/53dc445ee31c9bcc63c65420451ddfe3.png"
CHAPELEIRO = "https://1.bp.blogspot.com/-tAXkGMOWegk/VviGXWfyrTI/AAAAAAAARrY/GQw3qlEZ-z8djESn2fqer2Rctb0FyrCug/s1600/plano-de-aula-alice-no-pa%25C3%25ADs-das-maravilhas%252Cchapeleiro.gif"
FLORESTA = "https://img.elo7.com.br/product/zoom/12F2BAA/painel-de-festa-floresta-3-painel-em-tecido.jpg"
MESA = "https://vignette.wikia.nocookie.net/kingdomhearts/images/a/ac/Wonderland-_Tea_Party_Garden_%28Art%29_KH.png/revision/latest?cb=20131218033510"
CASA = "http://funforkids.ru/pictures/bg/bg021.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    mesa = Cena(img=MESA)
    casa = Cena(img=CASA)
    
    # passagem das páginas para o lado direito
    floresta.direita = mesa
    mesa.direita=casa
    
    # passagem das páginas o lado esquerdo. Voltando as páginas da história
    mesa.esquerda = floresta
    casa.esquerda = mesa
    
    # cria personagens
    tarzan=Elemento(img=TARZAN, tit="Tarzan" , style=dict(left=100, top=50, width=80, height=200))
    tarzan2 = Elemento(img=TARZAN, tit="Tarzan", style=dict(left=300, top=100, width=80, height=200))
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left=200, top=50, width=80, height=200))
    
    # mensagens dos personagens
    falatarzan = Texto(floresta, "Que fome !!!")
    tarzan.vai=falatarzan.vai
    
    tarzan.entra(floresta)
    tarzan2.entra(mesa)
    alice.entra(mesa)
    
    floresta.vai()
   
criarcenas()
    
    
    
