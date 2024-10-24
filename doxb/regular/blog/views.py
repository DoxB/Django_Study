from django.shortcuts import render

# Create your views here.

#
def main(request):
    return render(request, 'index.html')

# def pf_detail(request):
#     return render(request,'portfolio-details.html')

def pf_detail_gov(request):
    return render(request,'portfolio-details_gov.html')

def pf_detail_rag(request):
    return render(request,'portfolio-details_rag.html')

def pf_detail_univ(request):
    return render(request,'portfolio-details_univ.html')