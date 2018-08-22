# ida.callie.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
BARBIE = "https://i.imgur.com/21y2YUF.png"
TARZAN = "https://i.imgur.com/zgUuDIe.png"
HOMEM_ARANHA = "https://i.imgur.com/H5gr3qm.png"
FLORESTA = "https://i.imgur.com/ZjwoYBc.jpg"
CIDADE = "https://i.imgur.com/RqRv4YB.jpg"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    
    floresta.direita = cidade