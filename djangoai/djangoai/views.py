from django.shortcuts import render
from django.http import JsonResponse
from .client_socket import send_query_to_socket_server
from django.shortcuts import redirect



def index(request):
    return render(request, "index.html")

def ask_bot(request):
    if request.method == "POST":
        message = request.POST.get("message", "")
        if not message:
            return JsonResponse({"reply": "Mensaje vacío."})
        reply = send_query_to_socket_server(message)
        return JsonResponse({"reply": reply})
def chess_game(request):
    return redirect('/static/chess-ai-main/index.html')

def map_view(request):
    return render(request, "map.html")