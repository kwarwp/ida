# ida.courtney.main.py
from _spy.vitolino.main import Cena, Elemento, Texto
from _spy.vitolino.main import INVENTARIO as inv
TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
CINDERELA = "https://cdn.awsli.com.br/239/239279/produto/7143495/totens-displays-cinderela-64583d24.jpg"
ALICE = "https://upload.wikimedia.org/wikipedia/pt/thumb/7/72/Alice_Disney.jpg/220px-Alice_Disney.jpg"
HOMEM_ARANHA = "https://img.elo7.com.br/product/original/11FBB76/peso-de-porta-homem-aranha-spider-man-presentes.jpg"
FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
CASA = "http://1.bp.blogspot.com/-7CEY5DMNSDU/UnLHiLLQO7I/AAAAAAAAAUA/3xrMlvUTXzo/s1600/floresta-381288.jpg"
CASTELO = "https://png.pngtree.com/element_origin_min_pic/21/03/20/1656efb0f4aa630.jpg"
CHA = "https://deborawolf.files.wordpress.com/2012/10/picture-device-independent-bitmap-11.jpg"

def criarcenas():
    cha =Cena(img=CHA)
    floresta =Cena(img=FLORESTA)
    casa =Cena(img=CASA)
    castelo =Cena(img=CASTELO)
    cha.direita =floresta
    floresta.direita =CASA
    casa.direita =CASTELO

    cinderela =Elemento(img= CINDERELA, tit="Cinderela", style=dict(left=150, top=150, width=60,height=200)) 
    cinderela.entra(cha)
    ecinderela = Texto(cha, " boa tarde!")
    cinderela.vai=ecinderela.vai
    
    tarzan =Elemento(img= TARZAN, tit="Tarzan", style=dict(left=150, top=150, width=60,height=200))
    tarzan.entra(floresta)
    etarzan = Texto(floresta, " Ola!")
    tarzan.vai=etarzan.vai
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60,height=200))
    alice.entra(cha)
    ealice = Texto(cha, " vamos para casa!")
    alice.vai=ealice.vai
    
    homem_aranha =Elemento(img= HOMEM_ARANHA, tit="homem_aranha", style=dict(left=150, top=150, width=60,height=200))
    homem_aranha.entra(casa)
    ehomem_aranha = Texto(casa, " me acordaram!")
    homem_aranha.vai=ehomem_aranha.vai
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60,height=200))
    alice.entra(casa)
    ealice = Texto(casa, " vamos conhecer o castelo?")
    alice.vai=ealice.vai