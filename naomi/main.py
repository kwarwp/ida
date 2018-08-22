# ida.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
Cidade = "https://thumbs.dreamstime.com/b/arquitectura-da-cidade-azul-34467258.jpg"
Esgoto = "https://forbes.uol.com.br/wp-content/uploads/2018/04/esgoto-2.jpg"
Apartamento = "http://s2.glbimg.com/feWuUX0z-7pLnz4wnUSaw_fpglA=/smart/e.glbimg.com/og/ed/f/original/2016/02/01/apartamento-samy-e-ricky-lapa360-01.jpg"
Floresta = "https://ipc.digital/wp-content/uploads/2016/12/banho-de-floresta-640x360.jpg"
Homem_Aranha = "http://3.bp.blogspot.com/-uv54jlZoqfU/T9eUlpul_CI/AAAAAAAAFos/NCmWuK9X9Nw/s1600/Homem-Aranha-png-Queroimagem.com+%284%29.png"
Tarzan = "http://i82.photobucket.com/albums/j242/asia5/youngtarzan.png"
Barbie = "https://i.pinimg.com/originals/e7/b9/75/e7b975861052f57c15095b4e85304adc.png"

def criarcenas():
    floresta =Cena(img=Floresta)
    Homem_Aranha =Elemento(img= Homem_Aranha, tit="homiaranha", style=dict(left=150, top=150, width=60,height=200))
    Homem_Aranha.entra(floresta)
    Homem_Aranha.vai
    floresta.direita = cidade
    cidade =Cena(img=Cidade)
    cidade.direita = apartamento
    apartamento =Cena(img=Apartamento)
    Tarzan =Elemento(img= Tarzan, tit="Ex-marido da Jane", style=dict(left=150, top=150, width=60,height=200))
    eTarzan =Texto (Apartamento, "alguem me ajuda a sair daqui!!!!")
    Tarzan.vai=eTarzan.vai
    apartamento.direita = floresta
    floresta =Cena(img=Floresta)
    Homem_Aranha =Elemento(img= Homem_Aranha, tit="homiaranha", style=dict(left=150, top=150, width=60,height=200))
    floresta.direita = esgoto
    esgoto =Cena(img=Esgosto)
    Homem_Aranha =Elemento(img= Homem_Aranha, tit="homiaranha", style=dict(left=150, top=150, width=60,height=200))
    esgoto.direita = cidade
    cidade =Cena(img=Cidade)
    Barbie =Elemento(img= Barbie, tit="Boneca chata", style=dict(left=150, top=150, width=60,height=200))
    
    
    
    Floresta.vai()
criarcenas()
    
    