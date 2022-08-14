from django.shortcuts import redirect
from django.contrib import messages

from ..models.CompanyModel import CompanyModel

def delete_company_helper(request, companyID):
    user = request.user
    company = CompanyModel.objects.get(id=companyID)
    if user.id and user.username == company.owner.username:
        company.delete()
        messages.info(request, "Your document has been deleted")
        return redirect('tc_site:archive', username=user.username)
    else:
        messages.info(request, "You cannot perform this operation")
        return redirect('/')