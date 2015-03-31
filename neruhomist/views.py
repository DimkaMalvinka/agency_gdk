from django.shortcuts import render, get_object_or_404
from neruhomist.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse


def pagination(page, house_list):
    paginator = Paginator(house_list, 6) # Show 25 contacts per page
    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        houses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        houses = paginator.page(paginator.num_pages)
    return houses

def filtration(request):
    type1 = request.POST.get('type1')
    type2 = request.POST.get('type2')
    houses1 = House.objects.filter(house_type=type1).filter(sell_type=type2)
    if request.method =="POST":
        price_from = request.POST.get('price_from')
        price_to = request.POST.get('price_to')
        pl_from = request.POST.get('pl_from')
        pl_to = request.POST.get('pl_to')
        kimnat_from = request.POST.get('kimnat_from')
        kimnat_to = request.POST.get('kimnat_to')
        if price_from>'' and price_to>'':
           houses1 = houses1.filter(price__gte=price_from, price__lte=price_to)
        else:
            if price_from>'':
                houses1 = houses1.filter(price__gte=price_from)
            else:
                if price_to>'':
                    houses1 = houses1.filter(price__lte=price_to)

        if pl_from>'' and pl_to>'':
            houses1 = houses1.filter(ploshcha__gte=pl_from, ploshcha__lte=pl_to)
        else:
            if pl_from>'':
                houses1 = houses1.filter(ploshcha__gte=pl_from)
            else:
                if pl_to>'':
                    houses1 = houses1.filter(ploshcha__lte=pl_to)
        if kimnat_from>'' and kimnat_to>'':
           houses1 = houses1.filter(room_count__gte=kimnat_from, room_count__lte=kimnat_to)
        else:
            if kimnat_from>'':
                houses1 = houses1.filter(room_count__gte=kimnat_from)
            else:
                if kimnat_to>'':
                    houses1 = houses1.filter(room_count__lte=kimnat_to)    
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def index(request):
    kv_count = House.objects.filter(house_type=3).count()
    bud_count = House.objects.filter(house_type=4).count()
    com_count = House.objects.filter(house_type=5).count()
    zam_count = House.objects.filter(house_type=6).count()
    dil_count =House.objects.filter(house_type=6).count()
    in_count =House.objects.filter(house_type=7).count()
    return render(request, 'index.html', {'kv_count':kv_count,'bud_count':bud_count,'com_count':com_count,'zam_count':zam_count,'dil_count':dil_count,'in_count':in_count,})

def about(request):
    return render(request, 'about.html', {})

def poslugi(request):
    return render(request, 'poslug.html', {})

def karta(request):
    return render(request, 'karta.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def object(request, h_id):
    return render(request, 'object.html', {'house':House.objects.get(pk=h_id)})

def kvOrenda(request):
    houses1 = House.objects.filter(house_type=3).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 3
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def kvProdaj(request):
    houses1 = House.objects.filter(house_type=3).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 3
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def budOrenda(request):
    houses1 = House.objects.filter(house_type=4).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 4
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def budProdaj(request):
    houses1 = House.objects.filter(house_type=4).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 4
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def comOrenda(request):
    houses1 = House.objects.filter(house_type=5).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 5
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def comProdaj(request):
    houses1 = House.objects.filter(house_type=5).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 5
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def zamOrenda(request):
    houses1 = House.objects.filter(house_type=6).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 6
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def zamProdaj(request):
    houses1 = House.objects.filter(house_type=6).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 6
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def dilOrenda(request):
    houses1 = House.objects.filter(house_type=1).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 1
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def dilProdaj(request):
    houses1 = House.objects.filter(house_type=1).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 1
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def inOrenda(request):
    houses1 = House.objects.filter(house_type=7).filter(sell_type=1)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 7
    type2 = 1
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})

def inProdaj(request):
    houses1 = House.objects.filter(house_type=7).filter(sell_type=3)
    page = request.GET.get('page')
    houses = pagination(page, houses1)
    type1 = 7
    type2 = 3
    return render(request, 'search.html', {'houses':houses, 'type1':type1, 'type2':type2})
