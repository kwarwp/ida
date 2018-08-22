# ida.morgan.main.py
from_spy.vitolino.main import Cena, Elemento,Texto
from_spy.vitolino.main import Inventario as inve
PANTANO="https://www.google.com.br/search?safe=strict&hl=pt-BR&biw=1366&bih=662&tbm=isch&sa=1&ei=baR9W_WoKIauwATm5aaoCA&q=pantano+png&oq=PANTANO+PNG&gs_l=img.3.0.0.2433.2433.0.4904.1.1.0.0.0.0.90.90.1.1.0....0...1c.1.64.img..0.1.90....0.GtJGgSRkdAE#imgrc=FmpJ1aSDMsHI_M:"
ALICE="https://www.google.com.br/search?safe=strict&hl=pt-BR&biw=1366&bih=662&tbm=isch&sa=1&ei=c6R9W6ztE8aQwgTI3qnoCw&q=ALICE+png&oq=ALICE+png&gs_l=img.3..0l4j0i7i30k1l6.71970.75296.0.76462.12.9.0.0.0.0.148.886.2j6.8.0....0...1c.1.64.img..5.7.783...0i7i5i30k1j0i67k1j0i19k1j0i7i30i19k1.0.rZp-BAYZiOM#imgrc=X45qRiMKacN-AM:"
TARZAN="https://www.google.com.br/search?safe=strict&hl=pt-BR&biw=1366&bih=662&tbm=isch&sa=1&ei=wKR9W-HTMcX8wQTG-oKACg&q=TARZAN+png&oq=TARZAN+png&gs_l=img.3..0j0i7i30k1l5j0i5i30k1j0i7i30k1l2.55594.57340.0.58301.6.6.0.0.0.0.131.670.2j4.6.0....0...1c.1.64.img..0.6.667...0i19k1j0i7i30i19k1j0i7i5i30k1.0.6jfFeU2VQAs#imgrc=C9H7dFg-hoIvGM:"
YODA="https://www.google.com.br/search?safe=strict&hl=pt-BR&biw=1366&bih=662&tbm=isch&sa=1&ei=-6R9W-OIKoWqwASOta_IDA&q=YODA+png&oq=YODA+png&gs_l=img.3..0l2j0i7i30k1l8.100032.103099.0.106503.10.10.0.0.0.0.124.1066.1j9.10.0....0...1c.1.64.img..0.10.1062...0i7i5i30k1j0i19k1j0i7i30i19k1j0i67k1.0.HnPeGcqIZw4#imgrc=uEGvdKmP0d5uZM:"
PRAÇA="https://www.google.com.br/search?safe=strict&hl=pt-BR&biw=1366&bih=662&tbm=isch&sa=1&ei=ZqV9W7v7MYa4wATAvLTIBg&q=PRA%C3%87A+png&oq=PRA%C3%87A+png&gs_l=img.3..0j0i7i30k1l2j0i7i5i30k1j0i5i30k1.31421.34161.0.35917.9.8.0.0.0.0.172.881.3j5.8.0....0...1c.1.64.img..2.7.789...0i67k1.0.5hlH0eH-7bk#imgdii=ahSBxNT5zW_zRM:&imgrc=FeycxMbcjCnC3M:"

def criarcenas():
    pantano =Cena(img=PANTANO)
    praça =Cena(img=PRAÇA)
    pantano.direita = praça
    
    alice =Elemeto(img= ALICE, tit="Alice", style=dict(left=150, top=150, width=60, height=200)