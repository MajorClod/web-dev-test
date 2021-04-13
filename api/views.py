from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets
from rest_framework import permissions

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


from django.views.generic import TemplateView
class HomePage(TemplateView):
    template_name = 'index.html'