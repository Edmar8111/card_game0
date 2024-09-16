from django.shortcuts import render
from django.http import HttpResponse
from .models import Cards_db
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
lista_1=[]
@csrf_exempt
def home(request):
    from random import choice
    lista_0 = []
    
    card_behind_img = ''
    verso_card = ''
    bot_0 = 0
    cards_db = Cards_db.objects.all()
    #bug na requisição do verso do bot
    for a in cards_db:
        if a.id==3:
            bot_0 = a.id
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
    def teste():
        from random import randint
        overhead_bot = float(Cards_db.objects.get(id=bot_0).overhead)
        overhead_p = float(Cards_db.objects.get(id=lista_1[0]).overhead)
        if overhead_p>overhead_bot:
            print('Player Won')
        if overhead_p==overhead_bot:
            print('Draw')
        if overhead_p<overhead_bot:
            print('Player Lost')

    if request.method=='POST':
        #executa a function de request do front sem recarregamento de pagina e retorna valores
        import json
        data = json.loads(request.body)
        valor = int(data.get('valor'))
        if valor==1:
            #verificação de possivel requisição futura
            teste() 
          
    return render(request, 'base.html', {'cards_db':cards_db,'verso_card':verso_card,'card_behind':card_behind_img,
                                         'bot_card':Cards_db.objects.get(id=bot_0),
                                         'card_all':Cards_db.objects.get(id=lista_1[0])})