from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
from app1.models import Movie

from app1.forms import MovieForm

# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})


class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"

#get_query_set

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title="Manichithrathazhu")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__icontains="n")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__startswith="a")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__endswith="m")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(year__gt=2023)
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(year__lt=2024)
    #     return queryset

#get_context_data or extra_context

    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']="Arun"
    #     context['age']=23
    #     return context

    # extra_context={'name':'Arun','age':23}



def addmovie1(request): #built in form
    if(request.method=="POST"):   #After from submission
        form=MovieForm(request.POST,request.FILES) #Creates a form object using values that are passed through request.POST and request.FILES
        if form.is_valid():         #is_valid() built in function to check the values of form fields
            form.save()             #Save the form object in DB table
            return home(request) #redirects to homepage

    form=MovieForm()
    context={'form':form}
    return render(request,'add1.html',context)

# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES.get('i')
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')


class AddMovie(CreateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name='add1.html'
    success_url=reverse_lazy('app1:home')



# def detail(request,m):
#     k=Movie.objects.get(id=m)
#     return render(request,'detail.html',{'movie':k})


class Detail(DetailView):
    model=Movie
    template_name="detail.html"
    context_object_name="movie"


# def edit(request,e):
#     k=Movie.objects.get(id=e)
#
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         k.image=request.FILES.get('i')
#
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#
#         k.save()
#         return home(request)
#
#     return render(request,'edit.html',{'movie':k})

class Update(UpdateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name='edit.html'
    success_url=reverse_lazy('app1:home')

# def delete(request,i):
#     k=Movie.objects.get(id=i)
#     k.delete()
#     return home(request)

class Delete(DeleteView):
    template_name="delete.html"
    model=Movie
    success_url=reverse_lazy('app1:home')