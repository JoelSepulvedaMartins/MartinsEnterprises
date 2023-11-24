from django.shortcuts import render, redirect
from django.http import HttpResponse
from WebSite.models import Services
from datetime import datetime
# Create your views here.
def  index(request):
    return render(
        request,
        'WebSite/index.html'
    )
# View e function da pagina de serevicos
def nossos_servicos(request):
        if request.method == 'GET':  
            status = request.GET.get('status')
            print(status)

            return render(
                request,
                'WebSite/nossos_servicos.html',
                {'STATUS': status} ## Enviando variavel status para o html
                )
        elif request.method == 'POST':
            #Variaveis response form post
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            telephone = request.POST.get('telephone')
            
            #Criando uma instancia da model que ira se comunicar com o banco de dados
            service = Services(
                name = name,
                email = email,
                message = message,
                telephone = telephone,
                #data_created = datetime.now(),

            )
            #salvar a model em memoria no bancod e dados
            service.save()



            #colocando "?" depois do path vc consegue adicionar parametros
            #vc esta adicionando um valor a status que pode ser capturado pelo metodo get, por que vc vai estar renderizando a pag com GET
            return redirect("/nossos_servicos?status=1")
#View func Admin list service
def servicosAdmin(request):
    if request.method == 'GET':
        return render(request, 'WebSite/servicosAdmin.html',)
