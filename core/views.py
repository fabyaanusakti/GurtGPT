from django.shortcuts import render
from . import service
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_view(request):
    if 'chat' not in request.session:
        request.session['chat'] = []

    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')

        if prompt:
            response = service.response(prompt)
            request.session['chat'].append({
                'user': prompt,
                'gurt': response
            })
            request.session.modified = True

    context = {
        'chat': request.session.get('chat', [])
    }

    return render(request, 'index.html', context)