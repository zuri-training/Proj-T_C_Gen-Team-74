from django.shortcuts import render, redirect

def profile_helper (request):
    user = request.user

    if user.id:
        return render(request, 'tc_site/blocks/dashboard/profile.html')
    
    return redirect('/')