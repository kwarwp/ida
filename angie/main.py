# ida.angie.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 
ALICE = "https://icon2.kisspng.com/20180327/uue/kisspng-alice-liddell-alice-s-adventures-in-wonderland-the-alice-in-wonderland-5ab9ee8c10bb20.5426997015221346680685.jpg"
MESTRE_YODA = "https://vignette.wikia.nocookie.net/disney/images/9/95/Master_Yoda.png/revision/latest?cb=20161024220430&path-prefix=pt-br"
CINDERELA = "https://4.bp.blogspot.com/-c_4RlOC4vRk/WD8fPzbqbcI/AAAAAAAACA0/1ian8CfRW9o-HTtSpVWOU2AG1TmmkUY3QCLcB/s1600/Cinderella-Transparent-PNG.png"
FLORESTA = "https://vignette.wikia.nocookie.net/producaocultural/images/9/96/Floresta_Sombria.png/revision/latest?cb=20110605015107&path-prefix=pt-br" 
CIDADE = "https://www.rawstory.com/wp-content/uploads/2014/10/New-York-Central-Park-autumn-Shutterstock-800x430.png"

def criarcenas():
    floresta =Cena(img=FLORESTA)
    cidade =Cena(img=CIDADE) 
    floresta.direita = praia 
    cidade.esquerda = floresta 
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60, height=200))
    alice.entra(floresta)
    ealice = Texto(floresta, " Alice caminhava na floresta e estava perdida.Atormentada por seus pensamentos, imaginava todas coisas que poderiam estar acontecendo em sua casa.")
    alice.vai=ealice.vai
    
    
    
    
    deserto.vai
criarcenas()
    
   # yoda =Elemento(img= MESTRE_YODA, tit="Mestre Yoda", style=dict(left=150, top=150, width=50, height=150))
   # yoda.entra(floresta)
    
   # cinderela =Elemento(img= CINDERELA, tit="Cinderela", style=dict(left=150, top=150, width=60, height=200)) 