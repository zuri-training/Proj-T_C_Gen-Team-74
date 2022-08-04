from django.shortcuts import render

def coming_soon_helper(request):
    return render(request, 'tc_site/blocks/coming-soon.html')