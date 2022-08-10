from django.shortcuts import render

def profile_helper (request):
    return render(request, 'tc_site/blocks/dashboard/profile.html')