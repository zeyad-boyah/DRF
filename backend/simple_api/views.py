from django.http import JsonResponse

def api_home(request):
    return JsonResponse({'message':"hallo, welkommen von Django API"})
