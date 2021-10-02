from todo.forms import CreatorForm
# from django import db, forms
from todo.models import CreateModel
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# def home(request):

#     db_data = CreateModel.objects.all()
#     form = CreatorForm
#     if request.POST:
#         print('post')
#         form = CreatorForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             return redirect('/')

#     context = {
#         'db_data': db_data,
#         'form': form,
#     }

#     return render(request, 'home.html', context)


def home(request):
	tasks = CreateModel.objects.all()

	form = CreatorForm()

	if request.method =='POST':
		form = CreatorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'form':form, 'tasks':tasks}
	return render(request, 'home.html', context)

def update(request, pk):
	update_data = CreateModel.objects.get(id=pk)

	update_form = CreatorForm(instance=update_data)

	if request.POST:
		update_form = CreatorForm(request.POST, instance=update_data)
		if update_form.is_valid():
			update_form.save()
			return redirect('home')

	return render(request, 'update.html', {
		'update_form': update_form
	})		

# @csrf_exempt
def delete_tasks(request, pk):
    try:
        del_object = CreateModel.objects.filter(id=pk)
        del_object.delete()
        return redirect('home')
    except:
        print('delete error')

