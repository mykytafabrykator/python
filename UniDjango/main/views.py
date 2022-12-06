from django.shortcuts import render, redirect
from .models import Contacts, Certificates
from .forms import ContactsForm, CertificatesForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from .script import run
import mimetypes
from filestack import Client
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
class CertificatesDetailView(DetailView):
    model = Certificates
    template_name = 'main/details_view.html'
    context_object_name = 'certificate'

    def post(self, request, *args, **kwargs):
        p = list(request.path)
        id_dow = []
        if p[-1] == '/':
            p.pop()
        for i in p[::-1]:
            if i == '/':
                break
            else:
                id_dow.append(i)
        id_cert = ''.join(id_dow[::-1])
        get_data = Certificates.objects.filter(id = int(id_cert))
        name = get_data[0].name_surname
        course = get_data[0].course_name
        date = get_data[0].date
        place = get_data[0].place
        director = get_data[0].course_director
        run(id=id_cert, name_surname=name, course_name=course, date=date, place=place, course_director=director)
        # client = Client("API-KEY") - filestack file loading
        # new_filelink = client.upload(filepath=f'{id_cert}.pdf')
        # return redirect(new_filelink.url)
        try:
            with open(f'{id_cert}.pdf', 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
                return response
        except:
            return ('/')


def index(request):
    data = {
        'title': 'KEOA, FEL'
    }
    return render(request, 'main/index.html', data)


def certificate_search(request):
    error = 0
    if request.method == 'POST':
        id_cert = request.POST.get('q')
        try:
            b = Certificates.objects.get(pk=id_cert)
            return redirect(f'certificate/{id_cert}/')
        except:
            error = 'An error happenned'
    return render(request, 'main/search.html', {'error' : error})


@login_required(login_url='login')
def certificate_create(request):
    error = ''
    if request.method == 'POST':
        form = CertificatesForm(request.POST)
        if form.is_valid():
            form.save()
            created_id = Certificates.objects.latest('id')
            messages.success = f'Certificate was created successfully: {created_id}'
            return render(request, 'main/certificate_create.html', {'messages': messages.success})
        else:
            error = 'Form is invalid'

    form = CertificatesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/certificate_create.html', data)


@login_required(login_url='login')
def certificate(request):
    certificate_l = Certificates.objects.all()
    return render(request, 'main/certificate.html', {'certificate': certificate_l})


@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            error = 'Form is invalid'

    form = ContactsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


def contact(request):
    contact = Contacts.objects.all()
    data = {
        'title': 'Contacts',
    }
    return render(request, 'main/contact.html', {'data': data, 'contact': contact})