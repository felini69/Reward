from django.shortcuts import render
from contact.forms import ContactForm
from django.shortcuts import redirect
from django.views import View
from menu.models import MenuItem, FooterMenu
from extra.models import Logo, Analytics
from datetime import date
from .models import (
    FirstContainer, 
    SecondContainer, 
    ThirdContainer, 
    FourthContainer,
    FivethContainer,
    SixthContainer,
    SeventhContainer,
    EighthContainer,
    NinthContainer,
    TenthContainer,
    )

def main_page(request):
    menu              = MenuItem.objects.filter(parent=None, is_active=True) \
                        .order_by('order') \
                        .prefetch_related('children')
    footer            = FooterMenu.objects.all().first()
    analytic          = Analytics.objects.filter(is_active=True)

    first_container   = FirstContainer.objects.filter(is_active=True).first()
    second_container  = SecondContainer.objects.filter(is_active=True) \
                       .prefetch_related('cards') \
                       .order_by('created_at')
    third_container   = ThirdContainer.objects.filter(is_active=True) \
                       .prefetch_related('cards') \
                       .order_by('created_at')
    fourth_container  = FourthContainer.objects.filter(is_active=True) \
                        .prefetch_related('cards') \
                        .order_by('created_at')
    fifth_container   = FivethContainer.objects.filter(is_active=True) \
                        .prefetch_related('cards') \
                        .order_by('created_at')
    sixth_container   = SixthContainer.objects.filter(is_active=True) \
                        .prefetch_related('cards') \
                        .order_by('created_at')
    seventh_container = SeventhContainer.objects.filter(is_active=True).order_by('created_at')
    eighth_container  = EighthContainer.objects.filter(is_active=True).order_by('created_at').first()
    ninth_container   = NinthContainer.objects.filter(is_active=True).order_by('created_at')
    tenth_container   = TenthContainer.objects.filter(is_active=True).order_by('created_at').first()
    
    # Process the contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']
            print(f"Received contact form submission: {name}, {email}, {company}, {message}")
            form.save()
            return redirect('main:main_page')
    else:
        form = ContactForm()

    # Current year for footer
    current_year = date.today().year  

    # Logo for header and footer
    logo_header = Logo.objects.filter(position='header', is_active=True).first()
    logo_footer = Logo.objects.filter(position='footer', is_active=True).first()

    context = {
        'form': form,
        'menu': menu,
        'footer': footer,
        'analytic': analytic,
        'logo_header': logo_header,
        'logo_footer': logo_footer,
        'current_year': current_year,
        'first_container': first_container,
        'second_container': second_container,
        'third_container': third_container,
        'fourth_container': fourth_container,
        'fifth_container': fifth_container,
        'sixth_container': sixth_container,
        'seventh_container': seventh_container,
        'eighth_container': eighth_container,
        'ninth_container': ninth_container,
        'tenth_container': tenth_container,
    }
    
    return render(request, 'main/index.html', context)


# class MainPageView(View):
#     template_name = 'main/index.html'

#     def get(self, request, *args, **kwargs):
#         first_container = FirstContainer.objects.filter(is_active=True)
#         second_container = SecondContainer.objects.filter(is_active=True) \
#                             .prefetch_related('cards')             \
#                             .order_by('created_at')
#         third_container = ThirdContainer.objects.filter(is_active=True)  \
#                             .prefetch_related('cards')             \
#                             .order_by('created_at')

#         form = ContactForm()

#         context = {
#             'first_container': first_container,
#             'second_container': second_container,
#             'third_container': third_container,
#             'form': form,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         first_container = FirstContainer.objects.filter(is_active=True)
#         second_container = SecondContainer.objects.filter(is_active=True) \
#                             .prefetch_related('cards')             \
#                             .order_by('created_at')
#         third_container = ThirdContainer.objects.filter(is_active=True)  \
#                             .prefetch_related('cards')             \
#                             .order_by('created_at')

#         form = ContactForm()

#         context = {
#             'first_container': first_container,
#             'second_container': second_container,
#             'third_container': third_container,
#             'form': form,
#         }
#         return render(request, 'main/index.html', context)