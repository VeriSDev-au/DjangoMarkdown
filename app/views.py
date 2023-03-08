from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    # currentdir = (
    #     os.path.join(os.path.dirname(os.path.abspath(__file__)), "") + "test.md"
    # )

    readmefile = (
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
        + "README.md"
    )

    with open(readmefile) as f:
        content_readme = f.read()

    context = {"content_readme": content_readme}
    return render(request, "home.html", context)
