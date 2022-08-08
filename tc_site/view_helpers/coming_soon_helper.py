from django.shortcuts import render

def coming_soon_helper(request, page):
    if page =='dashboard':
        return render(request, 'tc_site/pages/dashboard/coming_soon.html')
    return render(request, 'tc_site/blocks/coming-soon.html')