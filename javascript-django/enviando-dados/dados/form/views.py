from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")

        print("id:", id)
        print("nome:", nome)
        print("sobrenome:", sobrenome)
        
        data = {
            "ok": True, 
            "reload": True,
        }
        return JsonResponse(data)   

    return render(request, "form/form.html", locals())