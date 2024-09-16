from django.shortcuts import render
from django.http import HttpResponse
from .models import Cards_db,Images
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
lista_1=[]
lista_life=[]
@csrf_exempt
def home(request):
    from random import choice
    lista_0 = []
    card_behind_img = ''
    verso_card = ''
    anima_investida=''
    bot_0 = 0
    image_db = Images.objects.all()
    cards_db = Cards_db.objects.all()
    #bug na requisição do verso do bot
    for a in cards_db:
        if a.id==3:
            bot_0 = a.id
    for b in image_db:
        anima_investida=b.images.url
    for c in cards_db:
        lista_0.append(c.id)
        #requisição de imagem para estilização
        if c.verso_card_img.url == '/image_cards/image_cards/verso_card_1.jpg':
            card_behind_img = c.verso_card_img.url
        if c.verso_card_img.url == '/image_cards/image_cards/verso_card_0.png':
            verso_card = c.verso_card_img.url
    if len(lista_1)>0 and request.method=='GET':
        #requisita a limpeza caso aja um recarregamento de pagina
        lista_1.clear()
    if len(lista_1)<=0:
        #assegura um valor unico ao card
        lista_1.append(choice(lista_0))
    if len(lista_life)>0 and request.method=='GET':
        #executa uma limpeza caso a pagina seja recarregada
        lista_life.clear()
    if len(lista_life)<=0:
        #certifica-se de efetuar um valor solido
        lista_life.append(int(Cards_db.objects.get(id=bot_0).life))
        lista_life.append(int(Cards_db.objects.get(id=lista_1[0]).life))
    def teste():
        #REQUISIÇÃO DE DANO DE PLAYERS EM MANUTENÇÃO
        from random import randint
        overhead_bot = float(Cards_db.objects.get(id=bot_0).overhead)
        overhead_p = float(Cards_db.objects.get(id=lista_1[0]).overhead)
        print(f'PLayer Life={lista_life[1]}, Bot Life:{lista_life[0]}')
        if overhead_p>overhead_bot:
            lista_life[0]=lista_life[0]-(overhead_p*randint(5,9))
            lista_life[1]=lista_life[1]-(overhead_bot*randint(0,6))
            print(f'Player_life={int(lista_life[1])}, Bot_life={int(lista_life[0])}')
        if overhead_p==overhead_bot:
            lista_life[0]=overhead_p*randint(0,6)
            lista_life[1]=overhead_bot*randint(0,6)
            print(f'Player_life={int(lista_life[1])}, Bot_life={int(lista_life[0])}')
        if overhead_p<overhead_bot:
            lista_life[1]=overhead_bot*randint(5,9)
            lista_life[0]=overhead_p*randint(0,6)
            print(f'Player_life={int(lista_life[1])}, Bot_life={int(lista_life[0])}')

    if request.method=='POST':
        #executa a function de request do front sem recarregamento de pagina e retorna valores
        import json
        data = json.loads(request.body)
        valor = int(data.get('valor'))
        if valor==1:
            #verificação de possivel requisição futura
            teste() 
          
    return render(request, 'base.html', {'cards_db':cards_db,'verso_card':verso_card,'card_behind':card_behind_img,
                                         'bot_card':Cards_db.objects.get(id=bot_0),'img_investida':anima_investida,
                                         'life_player':lista_life[1],
                                         'card_all':Cards_db.objects.get(id=lista_1[0])})