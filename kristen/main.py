# ida.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
TARZAN = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXXq2vvGGCZRQ7F_8MeygorCuf-CtZF9CXfoUegrRcNnoqK_K8"
BARBIE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUqpvOfTN1A1DupHXmSJa350IxMHIUe5ooBryqWdNPCdaH3FqrSVlJB5s"
ARANHA = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY8V7Bbk-uUkzfdCFuAUb6rl66GHu7n1347Oh980sQXw27-UtB"
GULOSEIMAS = "http://www.supimpagirl.com.br/wp-content/uploads/2017/08/alice-no-pa%C3%ADs-das-maravilhas-ilustras-disney5.png"
CASTELO = "https://vignette.wikia.nocookie.net/drama-total-fanon/images/a/af/Castelo.png/revision/latest/scale-to-width-down/640?cb=20160117202039&path-prefix=pt-br"
PANTANO = "https://vignette.wikia.nocookie.net/runescape2/images/3/3f/P%C3%A2ntano_de_Mort_Myre.png/revision/latest?cb=20120331195051&path-prefix=pt"
FLORESTA = "https://vignette.wikia.nocookie.net/grandchase/images/8/8d/Floresta_do_desafio_0.png/revision/latest?cb=20120218225645&path-prefix=pt-br"

def criarcenas():
    guloseimas =Cena(img=GULOSEIMAS)
    pantano =Cena(img=PANTANO)
    castelo =Cena(img=CASTELO)
    floresta =Cena(img=FLORESTA)
    floresta.direita = guloseimas
    guloseimas.esquerda= floresta
    floresta.direita = guloseimas
    guloseimas.direita= pantano
    pantano.direita= castelo

    
    tarzan =Elemento(img= TARZAN, tit="Tarzan", style=dict(left=150, top=150, width=60, height=200))
    aranha =Elemento(img= ARANHA, tit="Aranha", style=dict(left=140, top=140, width=55, height=190))
    barbie =Elemento(img= BARBIE, tit="Barbie", style=dict(left=135, top=135, width=40, height=180))
    
    tarzan.entra (floresta)
    tarzan.entra (guloseimas)
    aranha.entra (guloseimas)
    etarzan = Texto (guloseimas, "Olha, o Homem Aranha")
    tarzan.vai=etarzan.vai
    earanha = Texto (guloseimas, "Sim, sou eu mesmo!")
    aranha.vai=earanha.vai
    
    
    floresta.vai()
criarcenas()