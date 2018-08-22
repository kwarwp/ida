# ida.stacy.main.py
from _spy.vitollino.main import Cena, Elemento,Texto
from _spy.vitollino.main import INVENTARIO as inv

TARZAN = "https://banner2.kisspng.com/20180406/xrq/kisspng-disney-s-tarzan-youtube-kala-the-walt-disney-compa-the-jungle-book-5ac777960c48e7.4181314615230217180503.jpg"
ALICE = "https://i.pinimg.com/originals/53/dc/44/53dc445ee31c9bcc63c65420451ddfe3.png"
CHAPELEIRO = "https://1.bp.blogspot.com/-tAXkGMOWegk/VviGXWfyrTI/AAAAAAAARrY/GQw3qlEZ-z8djESn2fqer2Rctb0FyrCug/s1600/plano-de-aula-alice-no-pa%25C3%25ADs-das-maravilhas%252Cchapeleiro.gif"
FLORESTA = "https://img.elo7.com.br/product/zoom/12F2BAA/painel-de-festa-floresta-3-painel-em-tecido.jpg"
MESA = "https://vignette.wikia.nocookie.net/kingdomhearts/images/a/ac/Wonderland-_Tea_Party_Garden_%28Art%29_KH.png/revision/latest?cb=20131218033510"
CASA = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjtpoy2noHdAhUMl5AKHU1dCTYQjRx6BAgBEAU&url=https%3A%2F%2Fpt.pngtree.com%2Ffree-png-vectors%2Fdesenho-de-casa&psig=AOvVaw0iwEjF9ZGsavG6xEAVbcqV&ust=1535047151462445"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    mesa = Cena(img=MESA)
    casa = Cena(img=CASA)
    floresta.direita = mesa
    mesa.direita=casa
    
    tarzan=Elemento(img=TARZAN, tit="Tarzan" , style=dict(left=100, top=50, width=60, height=200))
    tarzan.entra(floresta)
    falatarzan = Texto(floresta, "Que fome !!!")
    tarzan.vai=falatarzan.vai
    
    floresta.vai()
   
criarcenas()
    
    
    
