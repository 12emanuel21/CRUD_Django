from django.shortcuts import render
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Empleado
from django.urls import reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from django.http import JsonResponse
import os
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
import logging





from django.shortcuts import  redirect
from . forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            for _, row in df.iterrows():
                Empleado.objects.create(
                   
                    # Agrega más columnas según tu modelo
                   
                    Nombre = row['Nombre'],
                    Apellido = row['Apellido'],
                    Edad = row['Edad'],
                    Email = row['Email'],
                    Generos = row['Sexo'],
                    Salario = row['Salario'],
                    
                    
                )
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'app_crud/upload.html', {'form': form})



def success(request):
    return render(request, 'app_crud/success.html')










class listaEmpleados(ListView):
    model = Empleado
    context_object_name = 'object_empleados'
    
    
    
"""  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_empleados'] = context['object_empleados'].filter(usuario=self.request.user) 
        context['count'] = context['object_empleados'].filter(completo=False).count()
        
        valor_buscado = self.request.GET.get('area_buscar') or ''
        if valor_buscado:
            context['object_empleados'] = context['object_empleados'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context  """
   

""" class detalles_empleado(DetailView):
    model = Empleado
    context_object_name = 'object_detalle'
    template_name = 'app_crud/detalles.html'  """
    

""" def detalles_empleado(request, id):
    try:
        empleado = Empleado.objects.get(id=id)
        data = {"empleado": empleado}
        return render(request, "app_crud/detalles.html", data)
    except Empleado.DoesNotExist:
        error_message = f"no existe ningún registro para la busqueda id: {id}"
        return render(request, "app_crud/empleado_list.html", {"error_message": error_message}) """


class crear_empleado(CreateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('listaEmpleados')
    
class editar_empleado(UpdateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('listaEmpleados')
    
class eliminar_empleado(DeleteView):
    model = Empleado
    context_object_name = 'deleteEmpleados'
    success_url = reverse_lazy('listaEmpleados')
    
    
def view_form_carga_masiva(request):
    return render(request, 'app_crud/form_carga_masiva.html')

""" 
def cargar_archivo(request):
    try:
        if request.method == 'POST':
            archivo_xlsx = request.FILES['archivo_xlsx']
            if archivo_xlsx.name.endswith('.xlsx'):
                df = pd.read_excel(archivo_xlsx, header=0)

                for _, row in df.iterrows():
                    Nombre = row['Nombre']
                    Apellido = row['Apellido']
                    Edad = row['Edad']
                    Email = row['Email']
                    Generos = row['Sexo']
                    Salario = row['Salario']

                    empleado, creado = Empleado.objects.update_or_create(
                        Email=Email,
                        defaults={
                            'Nombre': Nombre,
                            'Apellido': Apellido,
                            'Edad': Edad,
                            'Email': Email,
                            'Generos': Generos,
                            'Salario': Salario,
                            
                        }
                    )

                return JsonResponse({'status_server': 'success', 'message': 'Los datos se importaron correctamente.'})
            else:
                return JsonResponse({'status_server': 'error', 'message': 'El archivo debe ser un archivo de Excel válido.'})
        else:
            return JsonResponse({'status_server': 'error', 'message': 'Método HTTP no válido.'})

    except Exception as e:
        logging.error("Error al cargar el archivo: %s", str(e))
        return JsonResponse({'status_server': 'error', 'message': f'Error al cargar el archivo: {str(e)}'})


# Genera un nombre único para el archivo utilizando UUID y conserva la extensión.
def generate_unique_filename(file):
    extension = os.path.splitext(file.name)[1]
    unique_name = f'{uuid.uuid4()}{extension}'
    return SimpleUploadedFile(unique_name, file.read())
    
 """
 
def cargar_archivo(request):
    if request.method == 'POST':
        archivo_xlsx = request.FILES.get('archivo_xlsx')
        if archivo_xlsx and archivo_xlsx.name.endswith('.xlsx'):
            try:
                df = pd.read_excel(archivo_xlsx, header=0)
                empleados = []
                for _, row in df.iterrows():
                    empleado = Empleado(
                        Nombre=row['Nombre'],
                        Apellido=row['Apellido'],
                        Edad=row['Edad'],
                        Email=row['Email'],
                        Generos=row['Sexo'],
                        Salario=row['Salario']
                    )
                    empleados.append(empleado)
                Empleado.objects.bulk_create(empleados, ignore_conflicts=True)
                return JsonResponse({'status_server': 'success', 'message': 'Los datos se importaron correctamente.'})
            except Exception as e:
                logging.error("Error al cargar el archivo: %s", str(e))
                return JsonResponse({'status_server': 'error', 'message': f'Error al cargar el archivo: {str(e)}'})
        else:
            return JsonResponse({'status_server': 'error', 'message': 'El archivo debe ser un archivo de Excel válido.'})
    return render(request, 'listaEmpleados.html')