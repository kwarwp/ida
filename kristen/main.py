# ida.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
TARZAN1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXXq2vvGGCZRQ7F_8MeygorCuf-CtZF9CXfoUegrRcNnoqK_K8"
TARZAN2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXXq2vvGGCZRQ7F_8MeygorCuf-CtZF9CXfoUegrRcNnoqK_K8"
TARZAN3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXXq2vvGGCZRQ7F_8MeygorCuf-CtZF9CXfoUegrRcNnoqK_K8"
BARBIE1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUqpvOfTN1A1DupHXmSJa350IxMHIUe5ooBryqWdNPCdaH3FqrSVlJB5s"
BARBIE2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUqpvOfTN1A1DupHXmSJa350IxMHIUe5ooBryqWdNPCdaH3FqrSVlJB5s"
BARBIE3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUqpvOfTN1A1DupHXmSJa350IxMHIUe5ooBryqWdNPCdaH3FqrSVlJB5s"
ARANHA = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY8V7Bbk-uUkzfdCFuAUb6rl66GHu7n1347Oh980sQXw27-UtB"
ARANHA2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY8V7Bbk-uUkzfdCFuAUb6rl66GHu7n1347Oh980sQXw27-UtB"
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
    pantano.esquerda= guloseimas
    guloseimas.direita= pantano
    pantano.direita= castelo
    

    
    tarzan1 =Elemento(img= TARZAN1, tit="Tarzan1", style=dict(left=150, top=150, width=60, height=200))
    tarzan2 =Elemento(img= TARZAN2, tit="Tarzan2", style=dict(left=150, top=150, width=60, height=200))
    tarzan3 =Elemento(img= TARZAN3, tit="Tarzan3", style=dict(left=150, top=150, width=60, height=200))
    aranha =Elemento(img= ARANHA, tit="Aranha", style=dict(left=50, top=140, width=55, height=190))
    barbie1 =Elemento(img= BARBIE1, tit="Barbie1", style=dict(left=135, top=135, width=40, height=180))
    
    tarzan1.entra (floresta)
    tarzan2.entra (guloseimas)
    aranha.entra (guloseimas)
    etarzan1 = Texto (guloseimas, "Olha, o Homem Aranha")
    tarzan1.vai=etarzan1.vai
    earanha = Texto (guloseimas, "Sim, sou eu mesmo!")
    aranha.vai=earanha.vai
    barbie1.entra (pantano)
    ebarbie1 = Texto (pantano, "Socorro, alguém me ajude")
    barbie1.vai=ebarbie1.vai
    tarzan3.entra (pantano)
    
    
    
    
    floresta.vai()
criarcenas()