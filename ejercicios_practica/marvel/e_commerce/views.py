# Create your views here.
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from e_commerce.models import Comic


def comic_list_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        _queryset = Comic.objects.all()
        _data = list(_queryset.values()) if _queryset.exists() else []
        return JsonResponse(data=_data, safe=False, status=200)
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )
     
        
        
def comic_filter_stock_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_filter_stock_api_view")
        _queryset= Comic.objects.filter(stock_qty=5)
        _data= list(_queryset.values())
        return JsonResponse(data=_data, safe= False, status=200)
       
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )


def comic_filter_price_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_filter_price_api_view")
        
        _queryset= Comic.objects.filter(price__gt=3)
        _data=list (_queryset.values())
        return JsonResponse(data=_data, safe= False, status=200)
     

    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)


def comic_list_order_api_view(request):
    if request.method == 'GET':
        # Alumno:
        # Deberá completar el funcionamiento de este endpoint.
        # Seguir los pasos detallados en
        # el archivo de enunciado de tarea
        print("Endpoint: comic_list_order_api_view")
        _queryset= Comic.objects.order_by("marvel_id")
        _data=list(_queryset.values())
        return JsonResponse(data=_data,safe=False, status=200)
    else:
        return JsonResponse(data={"message": "Método HTTP no permitido."}, status=405)
