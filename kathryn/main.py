# ida.kathryn.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 
BARBIE  = "http://www.pngmart.com/files/4/Barbie-PNG-Image.png"
TARZAN  = "https://banner2.kisspng.com/20180501/ite/kisspng-tarzan-jane-porter-film-etsy-drawing-jane-5ae85eb3d5d6f8.1259494515251780358759.jpg"
HOMEM_ARANHA = "https://1.bp.blogspot.com/-fhZPiXXAr9c/V_-RoY-A8ZI/AAAAAAAAC04/09OJgAdU7QE3gUDGgVAsuqGU1q6JQI94ACLcB/s1600/spiderman-al-psicologo.jpg"
FLORESTA = "https://cdn5.colorir.com/desenhos/color/201101/22de012c2fb28550dac23c854385b189.png"
PRAIA = "https://banner2.kisspng.com/20180405/cve/kisspng-drawing-praia-5ac5c3722ee6f2.5189570815229100661921.jpg"
DESERTO = "https://1.bp.blogspot.com/-jGzUZ1_8tho/V8nrH1Wn3jI/AAAAAAAALuY/GnLTMfrmB3E4l26fjMHHyH0n9uAe1ZpvQCLcB/s640/reserva-de-agua-deserto-las-vegas.png"

def criarcenas():
    deserto =Cena(img=DESERTO)
    praia =Cena(img=PRAIA)
    deserto.direita = praia
    
    barbie =Elemento(img= BARBIE, tit="Barbie", style=dict(left=150, top=150, width=60,height=200))
    barbie.entra(deserto)
    ebarbie = Texto(deserto, " tudo bem?")
    barbie.vai=ebarbie.vai
    
    
    
