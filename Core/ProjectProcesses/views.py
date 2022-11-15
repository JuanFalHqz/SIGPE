import json
from _ast import Delete
from builtins import print

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Core.ProjectProcesses.forms import ProjectCreateForm
from Core.ProjectProcesses.models import Project


# Create your views here.
class ListViewProjects(ListView):
    template_name = 'List_projects.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # comun para todas las clases list
        context['title'] = 'Listado de Proyectos'
        context['singular'] = 'Proyecto'
        context['plural'] = 'Proyectos'
        context['url_create'] = reverse_lazy('project_create_root')
        context['url_delete'] = reverse_lazy('project_delete_root')
        # espesíficos
        context['projects'] = Project.objects.all()

        return context;


class CreateViewProjects(CreateView):
    template_name = 'Create_project.html'
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy('project_list_root')

    def post(self, request, *args, **kwargs):
        form = ProjectCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un proyecto'
        context['singular'] = 'Proyecto'
        context['plural'] = 'Proyectos'
        context['projects'] = Project.objects.all()
        context['url_success'] = reverse_lazy('project_list_root')
        context['action'] = 'add'
        return context


class UpdateViewProject(UpdateView):
    template_name = 'Create_project.html'
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy('project_list_root')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un proyecto'
        context['singular'] = 'Proyecto'
        context['plural'] = 'Proyectos'
        context['projects'] = Project.objects.all()
        context['url_success'] = reverse_lazy('project_list_root')
        context['action'] = 'edit'
        return context


class DeleteViewProject(DeleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un proyecto'
        context['singular'] = 'Proyecto'
        context['plural'] = 'Proyectos'
        context['projects'] = Project.objects.all()
        context['url_success'] = reverse_lazy('project_list_root')
        context['action'] = 'delete'
        return context

    def get(self, request):
        deleted = False
        errors = ''

        pk = request.GET.get('pk')
        list_to_deleted = request.GET.getlist('list_id[]')
        #Si hay lista con elementos a eliminar, se eliminan
        if(list_to_deleted):
            try:
                for item in list_to_deleted:
                    Project.objects.get(pk=item).delete()
                deleted = True
            except Exception as e:
                errors += str(e.__str__())
            data = {
                'deleted': deleted,
                'errors': errors,
            }
            return JsonResponse(data)
        try:
            Project.objects.get(pk=pk).delete()
            deleted = True
        except Exception as e:
            errors += str(e.__str__())
        data = {
            'deleted': deleted,
            'errors': errors,
        }
        # d = json.dumps(data)
        return JsonResponse(data)
