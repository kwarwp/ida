from _spy.ameixa.main import Cena 

A_NORTE = "https://i.imgur.com/aLEjWgB.png"
A_LESTE = "https://i.imgur.com/sivjAnO.png"
A_SUL = "https://i.imgur.com/otHJhF0.png"
def main():
    a_norte = Cena(img=A_NORTE)
    a_leste = Cena(img=A_LESTE, esquerda=a_norte)
    a_sul = Cena(img=A_SUL, esquerda=a_leste)

    a_norte.direita = a_leste
    a_leste.direita = a_sul
    a_leste.vai()
    
main()