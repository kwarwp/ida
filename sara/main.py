# ida.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"]=900
PANTANO = "https://1.bp.blogspot.com/-jALpqBrfBW4/VvvS6bpUnVI/AAAAAAAAATo/sd2gRUbk3tc-rdp8iPeEXCgz6LSQGjGzQ/s1600/Swamp%2BHouse.jpg"
ALICE = "https://3.bp.blogspot.com/-o7Y78sYGkjY/V6O1G7WysSI/AAAAAAAAMO8/IG0Q7cJKKcYA70fLNINSaLG02t9fQT52QCLcB/s1600/ALICE%2B%25283%2529.png"
TARZAN = "https://vignette.wikia.nocookie.net/vsbattles/images/6/68/Tarzan.png/revision/latest?cb=20170117061234"
YODA = "https://vignette.wikia.nocookie.net/disney/images/9/95/Master_Yoda.png/revision/latest?cb=20161024220430&path-prefix=pt-br"
AVENIDA = "https://3.bp.blogspot.com/-L6J4CqwyXWY/W2XD_sCVqhI/AAAAAAAA1Ck/dGexwCTuNsA3YCrC8vaQTb9lsY7dHDdugCLcBGAs/s1600/Ciclovia%2BAmaral%2BPeixoto%2B2.png"

def criarcenas():
    pantano =Cena(img=PANTANO)
    avenida =Cena(img=AVENIDA)
    pantano.direita = avenida
    
    alice =Elemento(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60,height=200))
    alice.entra(pantano)
    falaalice = Texto(pantano, " Em uma noite enluarada, Dona ALICE saiu para dar uma volta. Porém, durante o passeio, se perdeu no caminho e não enxergava nada a sua frente além de um pantamo assutador.Pensando em como sair daquela enrrascada, a pequena Alice não teve outra opção do que rezar, quando de repente...")
    alice.vai=falaalice.vai
    pantano.vai()
criarcenas()

    tarzan =Elemento(img= TARZAN, tit="Tarzan", style=dict(left=150, top=150, width=60,height=200))
    tarzan.entra(pantano)
    falatarzan = Texto(pantano, "-Oooo oooo  ooooo ooooo!!!!- Eis que surge o Tarzan, que indignou-se pela hora que a menina andava pela rua. -Que cê tá fazendo aqui? Tá tarde!")
    tarzan.vai=falatarzan.vai
    pantano.vai()
criarcenas()
    
    