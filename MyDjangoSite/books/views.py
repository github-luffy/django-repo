from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from MyDjangoSite.books.models import Book
from MyDjangoSite.books.forms import ContactForm
from django.core.mail import send_mail # send mail

# Create your views here.


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    errors = []
    if 'query' in request.GET:
        query = request.GET['query']
        if not query:  # query is null
            errors.append('Enter a search term.')
        elif len(query) > 20:
            errors.append('Please enter less 20 characters')
        else:
            books = Book.objects.filter(title=query)
            return render_to_response('search_results.html', locals())
    return render_to_response('search_form.html', {'errors': errors})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data  # cleaned_data is a dict
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),  # sender
            #     ['siteowner@example.com'],  # receiver
            # )
            return redirect('/contact-thanks/')  # chongdingxiang
    else:
        form = ContactForm(
            initial={'subject': "I love your site!"}  # mo ren zhi
        )  # checkout data,here is not valid
    return render(request, 'contact_form.html', {'form': form},)  # show error informatin


def contact_thanks(request):
    return render_to_response('contact_thanks.html', locals())
