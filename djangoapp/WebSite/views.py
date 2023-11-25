from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from WebSite.models import Services
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages

from faker import Faker

seedNumber = 10

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
        return formSendDb(request)


# TODO Rename this here and in `nossos_servicos`
def formSendDb(request):
    
    #Variaveis response form post
    type_service = request.POST.get('type_service')
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    telephone = request.POST.get('telephone')
    stat = request.POST.get('status')
    print(stat)
    #Criando uma instancia da model que ira se comunicar com o banco de dados
    service = Services(
        name = name,
        email = email,
        message = message,
        telephone = telephone,
        #date_created = datetime.now(), o DateTimeField(auto_now_add=True)

    )

    #salvar a model em memoria no bancod e dados
    service.save()


    #colocando "?" depois do path vc consegue adicionar parametros
    #vc esta adicionando um valor a status que pode ser capturado pelo metodo get, por que vc vai estar renderizando a pag com GET

        # jeito alternativo de pegar o form
    # Dados do formulário
    #   tentar dessa forma dpos
    #     # Dados do formulário
    #     data = {
    #         'tipo-servico': 'manutencao-preventiva',
    #         'name': request.POST.get('name'),
    #         'email': request.POST.get('email'),
    #         'telephone': request.POST.get('telephone'),
    #         'message': request.POST.get('message'),
    #     }

    #     # URL da view
    #     url = '/nossos_servicos'

    #     # Enviar a requisição POST usando requests.post
    #     response = requests.post(url, data=data)

    #     # Verificar se a requisição foi bem-sucedida
    #     if response.status_code == 200:
    #         print('Formulário enviado com sucesso!')
    #     else:
    #         print('Erro ao enviar o formulário:', response.status_code)

    #     return redirect("/nossos_servicos?status=1")


    return redirect("/nossos_servicos?status=1")



# #View func Admin list service
# def servicosAdmin(request):
    
#     if request.method == 'GET':
#         query_params = request.GET    
#         if  query_params.get('fitroDesejado'):
#             name_filter = query_params.get('fitroDesejado')
#             print("filtro")
#             services = Services.objects.filter(name=name_filter)
#         elif query_params.get('Pequisar'):
#             name_search = query_params.get('Pequisar')
#             print("pesquisa")

#             services = Services.objects.filter(name__contains=name_search)
#         else:
#             print("all")

#             services = Services.objects.all()
#         return render(request, 'WebSite/servicosAdmin.html', {'services': services}) # Enviando variável service para html



def filter_by_option(option, value):
    # Função para aplicar filtro com base na opção selecionada
    if option == 'name':
        services = Services.objects.filter(name=value)
    elif option == 'email':
        services = Services.objects.filter(email=value)
    elif option == 'dateSolicited':
        services = Services.objects.filter(date_created=value)
    elif option == 'telephone':
        services = Services.objects.filter(telephone=value)
    else:
        message = "Opção inválida"
        return None, message

    if not services.exists():
        message = "Nenhum resultado encontrado na database"
        return None, message
    message = "Encontrado com sucesso"
    return services, message

def search_by_option(option, value):
    # Função para aplicar pesquisa com base na opção selecionada
    if option == 'name':
        services = Services.objects.filter(name__contains=value)
    elif option == 'email':
        services = Services.objects.filter(email__contains=value)
    elif option == 'dateSolicited':
        services = Services.objects.filter(date_created__contains=value)
    elif option == 'telephone':
        services = Services.objects.filter(telephone__contains=value)
    else:
        message = "Opção inválida"
        return None, message

    if  services.exists():
        message = "Encontrado com sucesso"
        return services, message
    
    message = "Nenhum resultado encontrado na database, se tiver certeza de sua existencia, pode indicar algum erro"
    return None, message
    
def list_all_services(request):
    # Nenhuma opção ou pesquisa, lista todos os serviços
    services = Services.objects.all()
    typeRequisition = "=!=!=!=Listar Todos=!=!=!="
    return render(request, 'WebSite/servicosAdmin.html', {'services': services, 'typeRequisition': typeRequisition})

def servicosAdmin(request):
    if request.method == 'GET':
        query_params = request.GET
        print(query_params)
        if 'filtroDesejado' in query_params:
            # Aplica filtro se 'filtroDesejado' estiver presente
            name_filter = query_params.get('filtroDesejado')
            selected_option = query_params.get('selectedOption')          

            services, message = filter_by_option(selected_option, name_filter)
           
            typeRequisition = "=!=!=!=Filtrar Especifico=!=!=!="
        elif 'Pesquisar' in query_params:
            # Aplica pesquisa se 'Pesquisar' estiver presente
            temp_search = query_params.get('Pesquisar')
            selected_option = query_params.get('selectedOption')
            print(selected_option)
            print("pesquisa")
            services, message = search_by_option(selected_option, temp_search)
            typeRequisition = "=!=!=!=Pesquisar=!=!=!="
        else:
            # Nenhuma opção ou pesquisa, lista todos os serviços
            services = Services.objects.all()
            typeRequisition = "=!=!=!=Listar Todos=!=!=!="
            message = None
        return render(request, 'WebSite/servicosAdmin.html', {'services': services, 'typeRequisition': typeRequisition, 'message': message})
    if request.method == 'POST': ##TODO ARRUMAR ISSO DAQ PQ QUALQUER POST IRA GERAR 1500 USUARIOS NO BANCOD E DADOS
        if seedNumber < 10:
            message = "listando todos"
            seed_services()
        else:
            message = "listando 1500"
            
        services = Services.objects.all()
        typeRequisition = "=!=!=!=Listar Todos=!=!=!="
        return render(request, 'WebSite/servicosAdmin.html', {'services': services, 'typeRequisition': typeRequisition, 'message': message})



def serviceDelete(request, id):
    #TODO arrumar isso que ta tudo bagunçado com gambiarra
    # # SE QUISER ATUALIZAR/MUDAR OS DADOS:
    # service.email = "VcFoiMudado@Paunoseucu.com"
    # service.save()
    service = Services.objects.get(id=id)
    service.delete()
    messages.success(request, 'Serviço excluído com sucesso.')  

    return redirect('/servicosAdmin')
##Utilitarios para desenvovimento e testes


def see_service(request, id):
    service = Services.objects.get(id=id)

    return render(request, 'WebSite/serviceCrudeAdmin.html', {'service': service})






def seed_services(num_entries=1500):
    
    fake = Faker()
    for _ in range(num_entries):
        # Garante que o nome não ultrapasse 50 caracteres
        name = fake.name()[:50]

        # Garante que o e-mail não ultrapasse 150 caracteres
        email = fake.email()[:150]

        # Garante que a mensagem não ultrapasse 1000 caracteres
        message = fake.text(max_nb_chars=1000)

        # Garante que o telefone não ultrapasse 20 caracteres
        telephone = fake.phone_number()[:20]

        date_created = fake.date_time_this_year()
        service = Services(
        name = name,
        email = email,
        message = message,
        telephone = telephone,
        #date_created = datetime.now(), o DateTimeField(auto_now_add=True)

    )
        service.save()