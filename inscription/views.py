from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from django.conf import settings
from .models import Candidat
from .forms import CandidatForm
import os
# Remplacer weasyprint par xhtml2pdf
from xhtml2pdf import pisa

def accueil(request):
    return render(request, 'inscription/accueil.html')

def nouvelle_inscription(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            messages.success(request, "Votre inscription a été enregistrée avec succès.")
            return redirect('confirmation', pk=candidat.pk)
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CandidatForm()
        
    return render(request, 'inscription/formulaire.html', {'form': form})

def confirmation(request, pk):
    candidat = Candidat.objects.get(pk=pk)
    return render(request, 'inscription/confirmation.html', {'candidat': candidat})

def telecharger_recu(request, pk):
    candidat = Candidat.objects.get(pk=pk)
    
    # Générer le contenu HTML du reçu
    template = get_template('inscription/recu_pdf.html')
    html = template.render({'candidat': candidat})
    
    # Créer le PDF avec xhtml2pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="recu-{candidat.code_inscription}.pdf"'
    
    # Convertir HTML en PDF
    pisa_status = pisa.CreatePDF(
        html,                   # le HTML source
        dest=response,          # la destination (réponse HTTP)
    )
    
    # Renvoyer le PDF
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=400)
    return response

def verifier_statut(request):
    if request.method == 'POST':
        code = request.POST.get('code_inscription')
        try:
            candidat = Candidat.objects.get(code_inscription=code)
            return render(request, 'inscription/statut.html', {'candidat': candidat})
        except Candidat.DoesNotExist:
            messages.error(request, "Code d'inscription invalide")
        
    return render(request, 'inscription/verifier_statut.html')