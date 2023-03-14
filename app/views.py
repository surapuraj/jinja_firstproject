from django.shortcuts import render

# Create your views here.
def jinja_firstproject(request):
    dict={'name':'akhila','age':23}
    return render(request,'jinja_firstproject.html',context=dict)
