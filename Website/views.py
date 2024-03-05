from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Team
from .models import Publicite
from django.shortcuts import render, redirect
from .models import Contact , Newsletters
from django.contrib import messages

def home(request):
    publicites = Publicite.objects.all()
    teams = Team.objects.all()
    context = {'teams': teams, 'publicites': publicites}
    return render(request, 'Website/index.html', context)


def service(request):
    return render(request, 'Website/service.html')

from .models import Inscription
from .forms import InscriptionForm  # Create a Django form for your model

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('confirmation') # Redirect to a success page or any desired URL after successful form submission
    else:
        form = InscriptionForm()

    return render(request, 'Website/inscription.html', {'form': form})




def about(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'Website/about.html', context)



def contact(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire soumises par l'utilisateur
        nom = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('phone')
        sujet = request.POST.get('subject')
        message = request.POST.get('message')

        # Enregistrer les données dans la base de données
        new_contact = Contact(nom=nom, email=email, contact=contact, sujet=sujet, message=message)
        new_contact.save()
        return redirect('confirmation')
    return render(request, 'Website/contact.html')

def confirmation(request):
    return render(request, 'Website/confirmation.html')


def newsletters(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        if email:
            new_contact = Newsletters(email=email)
            new_contact.save()
            messages.success(request, 'Votre adresse e-mail a été enregistrée avec succès.')
        else:
            messages.error(request, 'Veuillez fournir une adresse e-mail valide.')

    return render(request, 'Website/contact.html')


def features(request):
    return render(request, 'Website/feature.html')

def team(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'Website/team.html',context)


def testimonial(request):
    return render(request, 'Website/testimonial.html')

def appoinment(request):
    return render(request, 'Website/appoinment.html')



from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'Website/404.html', status=404)
