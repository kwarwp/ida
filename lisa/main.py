# ida.lisa.main.py
# ida.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
CHA = "https://vignette.wikia.nocookie.net/disneyprincesas/images/e/ef/Alice-in-wonderland-disneyscreencaps.com-5785.jpg/revision/latest?cb=20140822145715&path-prefix=pt-br"
TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
ARANHA = "https://lumiere-a.akamaihd.net/v1/images/usa_spider-man_chi_spider-man_r_d909a17b.png?region=0%2C0%2C600%2C600"
FLORESTA = "https://img.elo7.com.br/product/zoom/12F2BAA/painel-de-festa-floresta-3-painel-em-tecido.jpg"
BARBIE = "http://www.pngmart.com/files/4/Barbie-Transparent-Background.png"
PANTANO = "https://gartic.com.br/imgs/mural/ca/catapimbador/pantano.png"
CASTELO = "https://vignette.wikia.nocookie.net/mlp/images/1/1b/Ponies_and_royal_guards_outside_the_castle_S03E13.png/revision/latest?cb=20130218113656"

def criarcenas():
    cha =Cena(img=CHA)
    floresta =Cena(FLORESTA)
    pantano =Cena(PANTANO)    
    castelo =Cena(CASTELO)
    
    floresta.direita = cha
    cha.esquerda = floresta
    cha.direita = pantano
    pantano.esquerda = cha
    pantano.direita = castelo
    castelo.esquerda = pantano
    
    barbie =Elemento(img= BARBIE, tit="Barbie", style= dict(left=150, top=150, width=60, height=200))
    tarzan =Elemento(img= TARZAN, tit="Tarzan", style= dict(left=100, top=100, width=70, heigh=200))
    aranha =Elemento(img= ARANHA, tit="Aranha", style= dict(left=170, top=100, width=60, height=180))
    
    tarzan.entra (floresta)
    aranha.entra (cha)
    earanha = Texto (cha, "eu mesmo!")
    tarzan.entra =(cha)
    etarzan = Texto (cha, "ouça esse som!")
    barbie.entra =(pantano)
    ebarbie = Texto (pantano, "SOCORRO, estou presa na areia movediça!")
    tarzan.entra =(pantano)
    etarzan = Texto (pantano, "eu te ajudo!")
    barbie.entra =(castelo)
    tarzan.entra =(castelo)
    ebarbie = Texto (castelo, "venha para um almoço de agradecimento!")
    tarzan.vai = etarzan.vai
    
 

    
    
    
    
    floresta.vai()
criarcenas()
    
    
    
    
  

