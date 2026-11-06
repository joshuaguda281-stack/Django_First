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
    hospital_name = "City Hospital"
    location = "123 Main Street, City"
    established_year = 1990
    contact = "+1 (555) 123-4567"
    email = "info@cityhospital.com"

    data = {
        'hospital_name': hospital_name,
        'location': location,
        'established_year': established_year,
        'contact': contact,
        'email': email
    }

    return render(request, 'about.html', data)