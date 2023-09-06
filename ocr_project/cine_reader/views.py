from django.shortcuts import render, redirect
from .forms import ImageForm
from django.http import HttpResponse
import sys
sys.path.append('..')
from reader import CineReader
ocr = CineReader(r"..\model\best_lite.pt")

# Create your views here.
def index(request):
    results = ("","")
    if request.method == 'POST':
        form = ImageForm(data = request.POST, files=request.FILES)
 
        if form.is_valid():
            form.save()
            images = form.instance
            recto, verso, rot = images.recto, images.verso, images.rot
            output = ocr([recto, verso], rot)
        return render(request,"result.html", {"output" : output})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
 