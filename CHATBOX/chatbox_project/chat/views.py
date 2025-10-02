from django.shortcuts import render
from django.http import JsonResponse
import json, re, random


with open("chat/responses.json") as f:
    responses = json.load(f)

def index(request):
    return render(request, "chat/index.html")


def get_response(request):
    user_message = request.GET.get("message")
    user_message = user_message.lower()
    for pattern, replies in responses.items():
        if re.search(pattern, user_message):
            return JsonResponse({"reply": random.choice(replies)})
    return JsonResponse({"reply":"Sorry i don't understand."})