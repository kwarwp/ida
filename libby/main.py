# ida.libby.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 

TARZAN = "https://banner2.kisspng.com/20180319/rpw/kisspng-toy-thumb-fictional-character-brown-hair-hand-tarzan-5ab053241310b6.3817319715215050600781.jpg"
HOMEM_ARANHA = "https://banner2.kisspng.com/20180619/fxt/kisspng-spider-man-television-fan-art-rendering-homem-aranha-5b289435b98b88.17202473152938603776.jpg"
PANTANO = "https://vignette.wikia.nocookie.net/monsterhunterespanol/images/2/2b/MHFU-Pantano.png/revision/latest?cb=20130503184351&path-prefix=es"
CIDADE = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/CentroRJ.jpg/1200px-CentroRJ.jpg"
LATA_DE_LIXO = "http://clipart.coolclips.com/480/vectors/tf05169/CoolClips_vc011404.png"
def criarcenas():
    cidade =Cena(img=CIDADE)
    pantano =Cena(img=PANTANO)
    cidade.direita = pantano
    
    homem_aranha =Elemento(img= HOMEM_ARANHA, tit="Homem_aranha", style=dict(left=150, top=150, width=60, height=200))
    homem_aranha.entra(cidade)
    lata_de_lixo =Elemento(img= LATA_DE_LIXO, tit="Lata_de_lixo", style=dict(right=150, top=130, width=40, height=180))
    lata_de_lixo.entra(cidade)
    falalata_de_lixo = Texto(cidade, "numa tarde nublada, incidentes misteriosos alarmavam a cidade")
    lata_de_lixo.vai=falalata_de_lixo.vai
    
    cidade.vai()
criarcenas()