from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'front_page.html')
def footer(request):
    return render(request,'footer.html')
def top_movies(request):
    return render(request,'top_movies.html')
def login_page(request):
    return render(request,'login_page.html')
def srk(request):
    return render(request,'info.html')
def disha(request):
    return render(request,'Disha.html')
def akshay(request):
    return render(request,'akshay.html')
def shraddha(request):
    return render(request,'shraddha.html')
def karthik(request):
    return render(request,'karthik.html')
def Deepika(request):
    return render(request,'Deepika.html')
def ayushmaan(request):
    return render(request,'ayushman.html')
def top_movies(request):
    return render(request,'top_movies.html')
def top_rated(request):
    return render(request,'top rated.html')
def upcoming(request):
    return render(request,'table.html')
