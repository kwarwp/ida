# ida.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv
TARZAN = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwig1qWUm4HdAhWCjZAKHaNpA8QQjRx6BAgBEAU&url=http%3A%2F%2Fvsdebating.wikia.com%2Fwiki%2FTarzan_(Disney)&psig=AOvVaw2Yms2xSKqXh6cUQQ4ri9jR&ust=1535046275059726"
BARBIE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiz6pnHm4HdAhXKFpAKHWhOA3cQjRx6BAgBEAU&url=https%3A%2F%2Fbr.pinterest.com%2Fpin%2F530158187378766638%2F&psig=AOvVaw0GLqkSoSV7WlkSIAKEPhG0&ust=1535046303517432"
ARANHA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjerJDZm4HdAhVDj5AKHf_-ANQQjRx6BAgBEAU&url=http%3A%2F%2Finspiracaopop.com.br%2Fhomem-aranha%2F&psig=AOvVaw2PKmQftzZwouM3MzZgXhvD&ust=1535046418197694"
GULOSEIMAS = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjeoKKPnIHdAhXKIZAKHZpWABQQjRx6BAgBEAU&url=http%3A%2F%2Fwww.supimpagirl.com.br%2Fbeda-alice-disney-ilustras%2F&psig=AOvVaw1GemHq7yPWk2-r_pGdmvxW&ust=1535046534375529"
CASTELO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjIzaaqnIHdAhVJhpAKHbJsA90QjRx6BAgBEAU&url=http%3A%2F%2Fpt-br.drama-total-fanon.wikia.com%2Fwiki%2FArquivo%3ACastelo.png&psig=AOvVaw0z7qQkd66UNZF8FLTJOsIw&ust=1535046582226979"
PANTANO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiy4969nIHdAhWLlJAKHc8tC2sQjRx6BAgBEAU&url=http%3A%2F%2Fpt.runescape.wikia.com%2Fwiki%2FFicheiro%3AP%25C3%25A2ntano_de_Mort_Myre.png&psig=AOvVaw0-DNFldM9eBA_Y_X14cyqs&ust=1535046628107721"
FLORESTA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiwysCOo4HdAhVDgJAKHTNDAoQQjRx6BAgBEAU&url=http%3A%2F%2Fpt-br.grandchase.wikia.com%2Fwiki%2FArquivo%3AFloresta_do_desafio_0.png&psig=AOvVaw1OJSdMoJWb5QyCj2F4uzFU&ust=1535048414320630"
def criarcenas():
    guloseimas =Cena(img=GULOSEIMAS)
    pantano =Cena(img=PANTANO)
    castelo =Cena(img=CASTELO)
    floresta =Cena(img=FLORESTA)
    floresta.direita = guloseimas
    guloseimas.esquerda=floresta
    floresta.direita = guloseimas
    guloseimas.direita= pantano

    
    tarzan =Elemento(img= TARZAN, tit="Tarzan", style=dict(left=150, top=150, width=60, height=200))
    aranha =Elemento(img= ARANHA, tit="Aranha", style=dict(left=150, top=150, width=60, height=200))
    barbie =Elemento(img= BARBIE, tit="Barbie", style=dict(left=150, top=150, width=60, height=200))
    
    tarzan.entra(floresta)
    aranha.entra(guloseimas)
    falatarzan = texto (guloseimas, "Olha, o Homem Aranha")
    tarzan.vai=falatarzan.vai
    falaaranha = texto (guloseimas, "Sim, sou eu mesmo!")
    aranha.vai=falaaranha.vai
    
    
    floresta.vai()
    criarcenas()