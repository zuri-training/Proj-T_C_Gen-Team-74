from django.contrib import messages
from django.shortcuts import redirect

from ..models.FeedBackModel import FeedBackModel


def feedback_helper(request):

    user = request.user

    if user.id:
        # Handle feedback data

        feedback = FeedBackModel(
            user=user,
            feedback=request.POST['feedback'],
            rating=request.POST['rating']
        )

        feedback.save()

        print(user.username)
        return redirect('tc_site:dashboard', username=user.username)

    messages.info(request, "You are not logged in. Try logging in first")
    return redirect('/')