from django.shortcuts import render
from django.views import View
from contact.forms import ContactForm
from django.shortcuts import redirect


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact/index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:success')
        context = {'form': form}
        return render(request, 'contact/index.html', context)


class ContactSuccessView(View):
    def get(self, request):
        return render(request, 'contact/success.html')




