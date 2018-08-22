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
    homem_aranha =Elemento(img= Homem_Aranha, tit="homiaranha" , style=dict(left=150, top=150, width=60,height=200))
    homem_aranha.entra(floresta)
    cidade =Cena(img=Cidade)
    floresta.direita = cidade
    apartamento =Cena(img=Apartamento)
    cidade.direita = apartamento
    tarzan =Elemento(img= Tarzan, tit="Ex-marido da Jane", style=dict(left=150, top=150, width=60,height=200))
    etarzan =Texto (Apartamento, "alguem me ajuda a sair daqui!!!!")
    tarzan.vai=etarzan.vai
    apartamento.direita = floresta
    floresta =Cena(img=Floresta)
    homem_aranha =Elemento(img= Homem_Aranha, tit="homiaranha", style=dict(left=150, top=150, width=60,height=200))
    floresta.direita = esgoto
    esgoto =Cena(img=Esgosto)
    homem_aranha =Elemento(img= Homem_Aranha, tit="homiaranha", style=dict(left=150, top=150, width=60,height=200))
    esgoto.direita = cidade
    cidade =Cena(img=Cidade)
    barbie =Elemento(img= Barbie, tit="Boneca chata", style=dict(left=150, top=150, width=60,height=200))
    
       
    floresta.vai()
criarcenas()
    
    