from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adoptions.models import AdoptionRequest, AdoptionPersonInfo
from apps.adoptions.forms import AdoptionRequestForm, PersonInfoForm
# Create your views here.


def adoptions_main(request):
    return HttpResponse('Adoptions Main Page')


class AdoptionRequestList(ListView):
    model = AdoptionRequest
    template_name = 'adoptions/AdoptionRequestList.html'


class AdoptionRequestCreate(CreateView):
    model = AdoptionRequest
    template_name = 'adoptions/AdoptionRequestForm.html'
    form_class = AdoptionRequestForm
    second_form_class = PersonInfoForm
    success_url = reverse_lazy('AdoptionRequestList')

    def get_context_data(self, **kwargs):
        context = super(AdoptionRequestCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            Request = form.save(commit=False)
            Request.adopter = form2.save()
            Request.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class AdoptionRequestUpdate(UpdateView):
    model = AdoptionRequest
    second_model = AdoptionPersonInfo
    template_name = 'adoptions/AdoptionRequestForm.html'
    form_class = AdoptionRequestForm
    second_form_class = PersonInfoForm
    success_url = reverse_lazy('AdoptionRequestList')

    def get_context_data(self, **kwargs):
        context = super(AdoptionRequestUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        requestadoption = self.model.objects.get(id=pk)
        personinfo = self.second_model.objects.get(id=requestadoption.adopter.id)

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=personinfo)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        request_id = kwargs.get('pk', 0)
        adoption_rec = self.model.objects.get(id=request_id)
        person_rec = self.second_model.objects.get(id=adoption_rec.adopter.id)
        form = self.form_class(request.POST, instance=adoption_rec)
        form2 = self.second_form_class(request.POST, instance=person_rec)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class UnlinkAdoptionRequest(DeleteView):
    model = AdoptionRequest
    template_name = 'adoptions/AdoptionRequestUnlink.html'
    success_url = reverse_lazy('AdoptionRequestList')

