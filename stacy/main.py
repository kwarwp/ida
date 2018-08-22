# ida.stacy.main.py
from _spy.vitollino.main import Cena, Elemento,Texto
from _spy.vitollino.main import INVENTARIO as inv
TARZAN = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi5trWunYHdAhUCj5AKHWd2A4sQjRx6BAgBEAU&url=https%3A%2F%2Fwww.kisspng.com%2Fpng-disney-s-tarzan-youtube-kala-the-walt-disney-compa-957952%2F&psig=AOvVaw2GYaTxjyq9TXQbldIZYhmL&ust=1535046871122431"
ALICE = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj9ivuDnIHdAhVEI5AKHQRICyAQjRx6BAgBEAU&url=http%3A%2F%2Fdocecantinhodare.blogspot.com%2F2015%2F11%2Falice-no-pais-das-maravilhas-png.html&psig=AOvVaw3l-7liDDOM4pvAJKdqluh6&ust=1535046507401857"
CHAPELEIRO = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiahK3RnIHdAhXFQpAKHRC-BWkQjRx6BAgBEAU&url=http%3A%2F%2Fmariafresa.net%2Fsingle%2F2265526.html&psig=AOvVaw2S7fwYVYWrVgnt-gYICKd1&ust=1535046650677203"
FLORESTA = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj0w5rmnYHdAhUBFJAKHbQEDBcQjRx6BAgBEAU&url=https%3A%2F%2Fwww.elo7.com.br%2Fpainel-de-festa-floresta-3%2Fdp%2F796515&psig=AOvVaw2-DB0f5pBANItO79sI3Jjs&ust=1535046952396508"
MESA = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiMzp6inoHdAhVFjpAKHUvnAlAQjRx6BAgBEAU&url=https%3A%2F%2Fcasamenteiras.casare.me%2F2009%2F05%2F30%2Falice-no-pais-das-maravilhas%2F&psig=AOvVaw1tgJLuP7oPOQDfseNH4y7W&ust=1535047095861794"
CASA = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjtpoy2noHdAhUMl5AKHU1dCTYQjRx6BAgBEAU&url=https%3A%2F%2Fpt.pngtree.com%2Ffree-png-vectors%2Fdesenho-de-casa&psig=AOvVaw0iwEjF9ZGsavG6xEAVbcqV&ust=1535047151462445"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    mesa = Cena(img=MESA)
    casa = Cena(img=CASA)
    floresta.direita = mesa
    mesa.direita=casa
    
    tarzan=Elemento(img=TARZAN, tit="Tarzan" , style=dict(left=100, top=50, width=60, height=200))
    tarzan.entra(floresta)
    falatarzan = Texto(floresta, "Que fome !!!)
    tarzan.vai=falatarzan.vai
    
    floresta.vai()
    
    
    
