from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/receipes/')

    querySet = Receipe.objects.all()


    context = {'receipes': querySet}

    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    return redirect('/receipes/')


def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)

    if(request.method == "POST"):
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description

        if(receipe_image):
            querySet.receipe_image = receipe_image

        querySet.save()
        return redirect("/receipes/")


    context = {'receipe' : querySet}
    return render(request, 'update_receipes.html', context) 
