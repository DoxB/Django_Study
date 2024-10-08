from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')  # templates 폴더 안의 index.html을 렌더링

def portfolio(request):
    return render(request, 'portfolio-details.html')  # templates 폴더 안의 portfolio-details.html을 렌더링

def service_details(request):
    return render(request, 'service-details.html')  # templates 폴더 안의 portfolio-details.html을 렌더링