from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def products(request):
    name = "Joshua Oluwaseun"
    age = 65
    weight = 70
    subjects = ['Math', 'Science', 'History', 'English',  'Art']
    isdisabled = True


    data = {
        'age': age,
        'weight': weight,
        'subjects': subjects,
        'isdisabled': isdisabled,
        'name': name
    }

    return render(request, 'products.html', data)

def about(request):
    return render(request, 'about.html')