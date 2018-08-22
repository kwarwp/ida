# ida.alexa.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
CASTELO = "https://http2.mlstatic.com/painel-lona-fosca-castelo-cinderela-3x2-envio-48hs-D_NQ_NP_405405-MLB25019727073_082016-F.jpg"
PRAIA = "https://png.pngtree.com/element_origin_min_pic/16/07/23/2257937d4f98949.jpg"
BARBIE = "https://i.pinimg.com/originals/db/f2/93/dbf293a3861d546eec5cab62d88325ec.png"
def criarcenas (): 
    castelo = Cena (img=CASTELO)
    praia = Cena (img=PRAIA)
    castelo.direita = praia
    praia.esquerda = castelo
    castelo.vai()
Barbie ()