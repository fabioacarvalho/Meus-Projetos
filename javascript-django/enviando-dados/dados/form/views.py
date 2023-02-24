from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    from form.models import Person
    if request.method == "POST":
        age = request.POST.get("age")
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")

        print("id:", id)
        print("nome:", nome)
        print("sobrenome:", sobrenome)

        item = Person.objects.create(
            name=nome,
            sobrenome=sobrenome,
            age=age
        )
        item.save()
        
        data = {
            "ok": True, 
            "reload": True,
        }
        return JsonResponse(data)   

    return render(request, "form/form.html", locals())


def grafico(request):
    
    return render(request, "form/grafico.html", locals())