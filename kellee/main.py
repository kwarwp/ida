# ida.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitolilino.main import INVENTARIO as inv
TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
HOMEM_ARANHA = "https://http2.mlstatic.com/adesivo-homem-aranha-recortado-cartela-1x1-D_NQ_NP_14475-MLB2822142047_062012-F.jpg"
BARBIE = "https://smedia.webcollage.net/rwvfp/wc/cp/22570011_legacycode/module/mattel/_cp/products/1447797951020/tab-14a8eb9f-1410-479a-adfc-e651c9f9cd95/e2a04254-4959-4127-af92-2b5424bb8646.png.w960.png"
FLORESTA = "https://img.elo7.com.br/product/original/12F2BDC/painel-de-festa-floresta-7-decoracao.jpg"
CASTELO = "https://cdn.shopify.com/s/files/1/2097/9875/products/Square-Disney-Castle_2734d77e-37c4-4ba3-abac-b41afcd0b753_1024x1024.png?v=1513204613"
PANTANO = "http://pluspng.com/img-png/swamp-png-hd-full-resolution-pluspng-com-png-swamp-1441.png"
MESA = "https://media-cdn.tripadvisor.com/media/photo-s/05/db/4c/20/hotel-fazenda-lagoa-azul.jpg"

def criarcenas ():
    floresta =Cena(img=FLORESTA)
    mesa =Cena(img=MESA)
    pantano =Cena(img=PANTANO)
    castelo =Cena(img=CASTELO)
    floresta.direita = mesa
    mesa.direita = pantano
    pantano.direita = castelo
    
    tarzan =Elemento(img= TARZAN, tit="Tarzan", style=dict(left=150, top=150, width=60,height=200))
    tarzan.entra(floresta)
    homem aranha =Elemento(img= HOMEM ARANHA, tit="Homem Aranha", style=dict(left=150, top=150, width=60,heigth=200))
    homem aranha.entra(mesa)
    barbie =Elemento(img= BARBIE, tit="Barbie", style=dict(left=150, top=150
    barbie.entra(pantano)
    falabarbie = Texto(deserto, "Socorro! Socorro! Estou na areia movediça!!")
    barbie.vai=falabarbie.vai
    
    
    
    
    pantano.vai()
criarcena()
   