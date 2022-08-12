from django.shortcuts import redirect
from django.contrib import messages

from ..models.DocumentModel import DocumentModel

def delete_doc_helper(request, docID):
    user = request.user
    document = DocumentModel.objects.get(id=docID)
    
    if user.id and (user.username == document.owner.username):
        document.delete()
        messages.info(request, "Your document has been deleted")
        return redirect('tc_site:archive', username=user.username)
    else:
        messages.info(request, "You cannot perform this operation")
        return redirect('/')