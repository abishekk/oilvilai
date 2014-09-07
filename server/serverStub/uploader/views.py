from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from .models import Document
from .forms import DocumentForm

def listall(request):
    form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def upload(request, uuid):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseBadRequest
    else:
        raise HttpResponseBadRequest
