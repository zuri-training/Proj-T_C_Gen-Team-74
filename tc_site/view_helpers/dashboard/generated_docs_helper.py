from django.shortcuts import render

def generated_docs_helper(request, username):

    return render(request, 'tc_site/blocks/coming-soon.html')
    # return render(request, 'tc-site/pages/dashboard/generated_docs.html')