# ida.callie.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
BARBIE = "https://i.imgur.com/21y2YUF.png"
TARZAN = "https://i.imgur.com/zgUuDIe.png"
HOMEM_ARANHA = "https://i.imgur.com/H5gr3qm.png"
FLORESTA = "https://i.imgur.com/ZjwoYBc.jpg"
CIDADE = "https://i.imgur.com/RqRv4YB.jpg"

def criarcenas():
    floresta =Cena(img=FLORESTA)
    cidade =Cena(img=CIDADE)
    floresta.direita = cidade
    
    homem_aranha =Elemento(img=HOMEM_ARANHA, tit="homemAranha", style=dict(left=150, top=150, width=60, height=200))
    homem_aranha.entra(floresta)
    falahomem_aranha = Texto(floresta, "Nossa! que isso? Estou numa floresta... como vim parar aqui?")
    homem_aranha.vai = falahomem_aranha.vai
    
    tarzan =Elemento(img=TARZAN, tit="tarzan", style=dict(left=150, top=150, width=60, height=200))
    tarzan.entra(cidade)
    falatarzan = Texto(cidade, "Poxa o homem-aranha disse que iria logo ali rapinho e estou aqui trancado no apartamento dele mais de 5h!")
    tarzan.vai = falatarzan.vai
    
    barbie = Elemento(img=BARBIE, tit="barbie", style=dict(left=150, top=150, width=60, height=200))
    barbie.entra(cidade)
    falabarbie = Texto(cidade, "Oi, homem-aranha!!! poderia ir numa festa comigo?")
    barbie.vai = falabarbie.vai

floresta.vai()
criarcenas()
