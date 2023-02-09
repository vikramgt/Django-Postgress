from django.shortcuts import redirect, render, get_object_or_404
from .models import Person
from .forms import CRUDFORM


def list_person(request):
    queryset = Person.objects.all().order_by('-first_name')
    context = {
        'queryset': queryset
    }
    return render(request, 'person_list.html', context)


def add_person(request):
    form = CRUDFORM(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('person_list')
    context = {
        "form":form
    }
    return render(request, 'add_person.html', context)





