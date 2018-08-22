# ida.angie.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE ["width"] = 1000
STYLE ["height"] = "600px"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
MESTRE_YODA = "https://vignette.wikia.nocookie.net/disney/images/9/95/Master_Yoda.png/revision/latest?cb=20161024220430&path-prefix=pt-br"
CINDERELA = "https://4.bp.blogspot.com/-c_4RlOC4vRk/WD8fPzbqbcI/AAAAAAAACA0/1ian8CfRW9o-HTtSpVWOU2AG1TmmkUY3QCLcB/s1600/Cinderella-Transparent-PNG.png"
FLORESTA = "https://vignette.wikia.nocookie.net/producaocultural/images/9/96/Floresta_Sombria.png/revision/latest?cb=20110605015107&path-prefix=pt-br" 
FLORESTA2 = "https://vignette.wikia.nocookie.net/producaocultural/images/9/96/Floresta_Sombria.png/revision/latest?cb=20110605015107&path-prefix=pt-br" 
CIDADE = "https://www.rawstory.com/wp-content/uploads/2014/10/New-York-Central-Park-autumn-Shutterstock-800x430.png"
CIDADE2 = "https://www.rawstory.com/wp-content/uploads/2014/10/New-York-Central-Park-autumn-Shutterstock-800x430.png"

def criarcenas():
    floresta =Cena(img=FLORESTA)
    floresta2 =Cena(img=FLORESTA2)
    cidade =Cena(img=CIDADE)
    cidade2 =Cena(img=CIDADE2)
    floresta.direita = floresta2
    floresta2.esquerda = floresta 
    floresta2.direita = cidade
    cidade.esquerda = floresta2 
    cidade.direita = cidade2
    cidade2.esquerda = cidade
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=500, top=150, width=200, height=100))
    alice.entra(floresta)
    ealice = Texto(floresta, "Alice caminhava na floresta e estava perdida. Atormentada por seus pensamentos, imaginava todas coisas que poderiam estar acontecendo em sua casa.")
    alice.vai=ealice.vai
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=200, top=150, width=200, height=200))
    alice.entra(floresta2)
    ealice = Texto(floresta2, "Então Alice, perdida na floresta, com seus pensamentos trevosos, encontra o Mestre Yoda.")
    alice.vai=ealice.vai
    yoda =Elemento(img= MESTRE_YODA, tit="Mestre Yoda", style=dict(left=60, top=150, width=100, height=70))
    yoda.entra(floresta2)
    eyoda = Texto(floresta2, "Vendo a aflição da menina, aconselha que ela tem que tirar férias na cidade")
    yoda.vai=eyoda.vai
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60, height=250))
    alice.entra(cidade)
    ealice = Texto(cidade, "Seguindo o conselho do Mestre Yoda, Alice foi para cidade tirar umas férias. ")
    alice.vai=ealice.vai
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=200, top=150, width=60, height=250))
    alice.entra(cidade2)
    ealice = Texto(cidade2, "Enquanto passeava em um belo parque cheio de árvores e pássaros, viu de longe Cinderela, cantando lindas canções, e acabou esquecendo de todos os seus problemas.")
    alice.vai=ealice.vai
    cinderela =Elemento(img= CINDERELA, tit="Cinderela", style=dict(left=20, top=150, width=150, height=300))
    cinderela.entra(cidade2)
    
    
    floresta.vai()
criarcenas()
    
 