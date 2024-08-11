from django.shortcuts import get_object_or_404, redirect, render
from . models import Articles
from . form import ArticleForm




def index(request, *args, **kwargs):
    article = Articles.objects.all()
    
    context = {
        'articles': article
    }
    return render(request, 'article/index.html', context)

# Ajout d'Articles

def add_Article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    messages = ""
    if request.method == "POST" and form.is_valid():
        form.save()
        form = ArticleForm()
        messages = "Ajout Effectuer avec succès!"
    return render(request, 'article/create.html', {'form': form, 'message': messages})


# Le Tableau

def tableau(request):
    table = Articles.objects.all()
    
    context = {
        'tables': table
    }
    return render(request, 'article/table.html', context)
    
    
    
# Modification

def modifer(request, my_id):
    obj = get_object_or_404(Articles, id=my_id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=obj)
    messages = ""
    if form.is_valid():
        form.save()
        form = ArticleForm()
        messages = "Modification effectuée avec succès"
    return render(request, 'article/update.html', {'form': form, 'message': messages})
        
# La suppression d'un article dans la base de données

def suppression(request, my_id):
    obj = get_object_or_404(Articles, id=my_id)
   # form = ArticleForm(request.POST or None, request.FILES or None, instance=obj)
    name = obj.name
    if request.method == "POST":
        obj.delete()
        return redirect("table")
    else:
        return render(request, 'article/delete.html')