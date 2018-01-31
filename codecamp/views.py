from django.shortcuts import render

# Create your views here.
def view(request):
    x = 'asdasd'
    return render(request, 'codecamp/jquery.html', {'x':x})



def ajax(request):
    return render(request, 'codecamp/ajax.html')