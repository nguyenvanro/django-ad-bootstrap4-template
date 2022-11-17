from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from core.models import UserAccount

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated == False:
            return render(request, 'auth/login.html', {})
        else:
            if request.user.is_superuser:
                count_user = UserAccount.objects.all().count()
                
                context = {
                    'count_user':count_user,
                }
                return render(request, 'home/index.html',context)
            else:
                count_user = UserAccount.objects.all().count()
                
                context = {
                    'count_user':count_user,
                }
                return render(request, 'home/index.html',context)
            
