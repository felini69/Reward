from django.shortcuts import render
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
    # Only show active items, in your prescribed order
    first_container = FirstContainer.objects.filter(is_active=True)
    second_container   = SecondContainer.objects.filter(is_active=True) \
                       .prefetch_related('cards')             \
                       .order_by('created_at')
    third_container    = ThirdContainer.objects.filter(is_active=True)  \
                       .prefetch_related('cards')             \
                       .order_by('created_at')
    context = {
        'first_container': first_container,
        'second_container': second_container,
        'third_container': third_container,
    }
    return render(request, 'main/index.html', context)
