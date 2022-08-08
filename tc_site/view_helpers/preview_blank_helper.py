from django.shortcuts import render

def preview_blank_helper(request):
    ctx = {
        'show_blank_preview': True
    }
    return render(request, 'tc_site/pages/landing/landing.html', ctx)