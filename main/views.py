from django.shortcuts import render
from contact.forms import ContactForm
from django.shortcuts import redirect
from .models import (
    FirstContainer, 
    SecondContainer, 
    SecondContainerCards, 
    ThirdContainer, 
    ThirdContainerCards,
    FourthContainer,
    FourthContainerCards,
    FivethContainer,
    FivethContainerCards,
    SixthContainer,
    SixthContainerCards,
    SeventhContainer,
    SeventhContainerCards,
    EighthContainer,
    NinthContainer,
    TenthContainer,
    )

def main_page(request):
    first_container = FirstContainer.objects.filter(is_active=True)
    second_container   = SecondContainer.objects.filter(is_active=True) \
                       .prefetch_related('cards')             \
                       .order_by('created_at')
    third_container    = ThirdContainer.objects.filter(is_active=True)  \
                       .prefetch_related('cards')             \
                       .order_by('created_at')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main_page')  # Redirect to the main page after saving
    else:
        form = ContactForm()

    context = {
        'first_container': first_container,
        'second_container': second_container,
        'third_container': third_container,
        'form': form,
    }
    return render(request, 'main/index.html', context)
