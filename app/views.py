from app.models 	import *
from app.forms 		import ContactoForm, BuscarForm
from django.shortcuts import render_to_response
from django.template 	import RequestContext
from django.core.mail import send_mail
import json


def index(request):
	buscar_form = BuscarForm()
	return render_to_response('index.html', locals() , context_instance=RequestContext(request))


def productos(request):
	medidas = Medidas.objects.all()
	neumaticos = Neumatico.objects.all()
	return render_to_response('productos.html', locals() , context_instance=RequestContext(request))


def busqueda(request):
	resultados = []
	if request.method == 'POST':
		buscar = BuscarForm(request.POST)
		if buscar.is_valid():
			tipos = buscar.cleaned_data['tipos']
			altura = buscar.cleaned_data['altura']
			ancho = buscar.cleaned_data['ancho']
			aro = buscar.cleaned_data['aro']

			resultados = Neumatico.objects.filter(medidas__ancho=385)
			nombre = resultados.name
	return HttpResponse (nombre)

def contacto(request):
	info_env = False
	descripcion = Personal.objects.all()
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			nombre = formulario.cleaned_data['nombre']
			correo = formulario.cleaned_data['correo']
			sitio_web = formulario.cleaned_data['sitio_web']
			mensaje = formulario.cleaned_data['mensaje']
			info_env = True
			send_mail('Cubiertasalabrenga.com', mensaje, correo,
     					['softwarelaycho@gmail.com'], fail_silently=False)
	else:
		formulario = ContactoForm()
	return render_to_response('contacto.html', {'form':formulario, 'info_env':info_env, 'descripcion':descripcion}, context_instance=RequestContext(request))



def ajax(request):
	if request.method == "POST":
		pk = int(request.POST['tipos'])

		altura = request.POST['altura']
		ancho = request.POST['ancho']
		aro = request.POST['aro']
		di = { 'altura' : [] , 'ancho':[], 'aro':[]}
		if altura == '':
			for i in Neumatico.objects.all():
				if i.categoria_id == pk:
					di['altura'].append(str(i.medidas.altura))
					# di['ancho'].append(str(i.medidas.ancho))
					# di['aro'].append(str(i.medidas.aro))
		elif altura != '':
			a = Medidas.objects.filter(altura=altura)
			if len(a) > 0:
				for i in a:
					di['ancho'].append(str(i.ancho))

		if  altura != '' and ancho != '':
			an = Medidas.objects.filter(altura=altura, ancho=ancho)
			if len(an) > 0 :
				for i in an:
					di['aro'].append(str(i.aro))

        js = json.dumps(di)

	return HttpResponse(js, content_type="application/json")
