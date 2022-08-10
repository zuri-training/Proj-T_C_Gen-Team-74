from django.shortcuts import render

def about_helper(request):
    return render(request, 'tc_site/blocks/about/about.html')