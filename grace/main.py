# ida.roxanne.main.py
#Em uma bela tarde a Alice ficou perdida no pântano.
#Quando foi encontrada pelo Tarzan
#Os dois voltando ao castelo, encontraram o Homem-aranha.
#Onde o Homem aranha estava passeando com a Barbie na cidade.
#Quando o homem aranha contou para a Barbie que era filho do Yoda.
#Eles viveram felizes para sempre

from  _spy.vitolino.main import Cena, Elemento, Texto
from _syp.vitolino.main import INVENTARIO as inv
HOMEM_ARANHA = "https://vignette.wikia.nocookie.net/marvel/images/2/2e/Homem-aranha.png/revision/latest?cb=20141112195415&path-prefix=pt-br"
TARZAN = "https://banner2.kisspng.com/20180501/ite/kisspng-tarzan-jane-porter-film-etsy-drawing-jane-5ae85eb3d5d6f8.1259494515251780358759.jpg"
YODA = "https://banner2.kisspng.com/20180202/lzq/kisspng-yoda-darth-maul-star-wars-jedi-star-wars-transparent-background-5a7487326a2b16.7780970115175862264349.jpg"
BARBIE = "https://icon2.kisspng.com/20180402/uaw/kisspng-barbie-a-fashion-fairytale-ballet-clip-art-barbie-5ac1e5f0320ce3.916858761522656752205.jpg"
ALICE = "https://icon2.kisspng.com/20180327/uue/kisspng-alice-liddell-alice-s-adventures-in-wonderland-the-alice-in-wonderland-5ab9ee8c10bb20.5426997015221346680685.jpg"
CIDADE = "https://www.nycgo.com/images/venues/2238/times-square-bus-7th-ave-brad-ogbonna__x_large.jpg"
PANTANO = "https://eucontista.files.wordpress.com/2015/10/pantano-306619.jpg"
CASTELO = "https://http2.mlstatic.com/mega-banner-painel-decoraco-castelo-240-x-150-mts-D_NQ_NP_880090-MLB25838655185_082017-F.jpg"
def criarcenas():
    cidade =Cena(img=CIDADE)
    castelo =Cena(img=CASTELO)
    cidade.direita = castelo
    
    alice = Elemento(img = ALICE, tit="Alice",style =dict(left=150 , top=150, width=60, height=200))
    alice.entra(pantano)
    ealice = Texto(pantano,"help help")
    alice.vai=ealice.vai
    
    pantano.vai()
criarcenas()