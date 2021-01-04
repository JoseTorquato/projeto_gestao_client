from django.shortcuts import render, redirect, get_object_or_404

from .models import Person
from .forms import PersonForm


def person_list(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'person.html', context)


def person_new(request):
    form = PersonForm(request.POST or None)  # instanciar form
    if form.is_valid():
        form.save()
        return redirect('person_list')
    context = {
        'form': form
    }

    return render(request, 'person_form.html', context)


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')

    context = {
        'form': form
    }
    return render(request, 'person_form.html', context)


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    context = {
        'form': form,
        'person': person
    }

    return render(request, 'person_delete_confirm.html', context)
