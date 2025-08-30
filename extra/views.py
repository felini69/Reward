from django.shortcuts import render
from .models import Terms

def terms_view(request):
    terms = Terms.objects.filter(is_active=True).first()
    return render(request, 'extra/terms.html', {'terms': terms})
