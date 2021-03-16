import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    numbers = random.sample(range(1, 46), 6)
    context = {
        'numbers': numbers
    }
    return render(request, 'lotto.html', context)