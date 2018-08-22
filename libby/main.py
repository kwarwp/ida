# ida.libby.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 

TARZAN = "https://banner2.kisspng.com/20180319/rpw/kisspng-toy-thumb-fictional-character-brown-hair-hand-tarzan-5ab053241310b6.3817319715215050600781.jpg"
HOMEM_ARANHA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_aranha_spider_man_homem_aranha_de_volta_ao_lar_spider_man_homecoming_movie_ma_21001_1_20170619150009.jpg"
PANTANO = "https://vignette.wikia.nocookie.net/monsterhunterespanol/images/2/2b/MHFU-Pantano.png/revision/latest?cb=20130503184351&path-prefix=es"
CIDADE = "http://www.revistaadventista.com.br/wp-content/uploads/2016/01/Campo-ou-cidade-1024x683.jpg"
LATA_DE_LIXO = "http://clipart.coolclips.com/480/vectors/tf05052/CoolClips_envi0011.png"
def criarcenas():
    cidade =Cena(img=CIDADE)
    pantano =Cena(img=PANTANO)
    cidade.direita = pantano
    
    homem_aranha =Elemento(img= HOMEM_ARANHA, tit="Homem_aranha", style=dict(left=150, top=120, width=60, height=200))
    homem_aranha.entra(cidade)
    lata_de_lixo =Elemento(img= LATA_DE_LIXO, tit="Lata_de_lixo", style=dict(right=150, top=50, width=30, height=20))
    lata_de_lixo.entra(cidade)
    falalata_de_lixo = Texto(cidade, "num fim de tarde, incidentes misteriosos alarmavam a cidade")
    lata_de_lixo.vai=falalata_de_lixo.vai
    
    cidade.vai()
criarcenas()