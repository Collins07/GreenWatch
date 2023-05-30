
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from .models import Forest, Reason
from django.contrib import messages
from django.core.paginator import Paginator
# from .userpreferences.models import UserPrefrence
import json


# Create your views here.
def search_forest(request):
    if request.method == 'POST':
      search_str=json.loads(request.body).get('searchText')
      forest = Forest.objects.filter(
          trees_planted__istartswith=search_str) | Forest.objects.filter(
          date__istartswith=search_str) | Forest.objects.filter(
          description__icontains=search_str)
      data = forest.values()
      return JsonResponse(list(data), safe=False)




def forest(request):
    categories = Reason.objects.all()
    forest = Forest.objects.all()

    paginator=Paginator(forest, 4)
    page_number = request.GET.get('page')
    page_obj= Paginator.get_page(paginator,page_number)
    context = {
        'forest': forest,
        'page_obj': page_obj,

    }
    return render(request, 'forests/index.html', context)


def add_forest(request):
    reasons = Reason.objects.all()
    context = {
        'reasons': reasons,
        'values': request.POST,
    }

    # if request.method == 'GET':
    #     trees_planted = request.POST['trees_planted']
    
    if request.method == 'POST':
        trees_planted = request.POST['trees_planted']

        if not trees_planted:
            messages.error(request,'Number of trees replaced required !!!')
            return render(request, 'forests/add_forest.html', context)
        description = request.POST['description']
        date = request.POST['date']

        
    if request.method == 'POST':
        description = request.POST['description']

        if not description:
            messages.error(request,' The name of your group is required !!!')
            return render(request, 'forests/add_forest.html', context)
        
        Forest.objects.create(owner=request.user, trees_planted=trees_planted, description=description, date=date)
        messages.success(request, 'Data saved successfully')

        return redirect('forest')

    return render(request, 'forests/add_forest.html', context)



def forest_edit(request, id):
    forest = Forest.objects.get(pk=id)
    reasons = Reason.objects.all()

    context = {
        'forest': forest,
        'values': forest,
        'reasons': reasons
    }
    if request.method == 'GET':
        
        return render(request, 'forests/edit_forest.html', context)
    if request.method == 'POST':
        trees_planted = request.POST['trees_planted']

        if not trees_planted:
            messages.error(request,'Number of trees replaced required !!!')
            return render(request, 'forests/edit_forest.html', context)
        description = request.POST['description']
        date = request.POST['date']
 
        
    if request.method == 'POST':
        description = request.POST['description']

        if not description:
            messages.error(request,' The name of your group is required !!!')
            return render(request, 'forests/edit_forest.html', context)
        

        forest.trees_planted=trees_planted
        forest.description=description
        forest.date=date

        forest.save()
        messages.success(request, 'Your data has been updated successfully')

        return redirect('forest')



def forest_delete(request,id):
    forest = Forest.objects.get(pk=id)
    forest.delete()
    messages.error(request, 'Your data has been deleted')
    return redirect('forest')