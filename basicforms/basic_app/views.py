from django.shortcuts import render
from  . import forms

def index(request):
    return render(request,'basic_app/index.html')

def forms_page(request):
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('Textarea: '+form.cleaned_data['text'])

    return render(request,'basic_app/form_page.html',{'form':form})
