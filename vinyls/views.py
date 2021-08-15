from django.shortcuts import render, get_object_or_404
from .models import Vinyls
from .filters import VinylFilter


app_name = 'vinyls'

def index(request):
    vinyls = Vinyls.objects.all()
    vinylFilter = VinylFilter(request.GET, queryset=vinyls)
    vinyls = vinylFilter.qs
    context = {'vinyls': vinyls, 'vinylFilter': vinylFilter}
    return render (request, 'vinyls/index.html', context)

def detail(request, vinyls_id):
    vinyl = get_object_or_404(Vinyls, pk=vinyls_id)
    context = {'vinyl': vinyl}
    return render(request, 'vinyls/detail.html',context)
