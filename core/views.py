from django.shortcuts import render
from . import service
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_view(request):

    response = None
    prompt = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        response = service.response(prompt)

    context = {
        'response': response,
        'prompt': prompt,
    }

    return render(request, 'index.html', context)