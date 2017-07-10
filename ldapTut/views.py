from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def public(request):
    return HttpResponse("Welcome to public page")

@login_required
def private(request):
    return HttpResponse("Welcome to private page")