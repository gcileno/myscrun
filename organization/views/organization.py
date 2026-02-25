from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class OrganizationView(View):
    def get(self, request):
        return render(request, 'organization/organization.html')
    
    def post(self, request):
        return HttpResponse('Organization created')