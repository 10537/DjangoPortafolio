from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.pets.forms import PetsForm
from apps.pets.models import Pets
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def pets_main(request):
    return render(request, 'pets/index.html')

# ~ Views as Functions

def pets_form(request):
    if request.method == 'POST':
        form = PetsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pets/')
    else:
        form = PetsForm()

    return render(request, 'pets/petsForm.html', {'form': form})


def pets_list(request):
    pets = Pets.objects.all().order_by('id')
    context = {'Pets': pets}

    return render(request, 'pets/petsList.html', context)


def pets_edit(request, reg_id):
    pet = Pets.objects.get(id=reg_id)
    if request.method == 'GET':
        form = PetsForm(instance=pet)
    else:
        form = PetsForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/pets/list')
    return render(request, 'pets/petsForm.html', {'form': form})


def pets_unlink(request, reg_id):
    pet = Pets.objects.get(id=reg_id)
    if request.method == 'POST':
        pet.delete()
        return HttpResponseRedirect('/pets/list')
    return render(request, 'pets/petsUnlink.html', {'Pet': pet})

# ~ Views as Class

class PetsNew(CreateView):
    model = Pets
    form_class = PetsForm
    template_name = 'pets/petsForm.html'
    success_url = reverse_lazy('PetsList')


class PetsUpdate(UpdateView):
    model = Pets
    form_class = PetsForm
    template_name = 'pets/petsForm.html'
    success_url = reverse_lazy('PetsList')


class PetsUnlink(DeleteView):
    model = Pets
    template_name = 'pets/petsUnlink.html'
    success_url = reverse_lazy('PetsList')
