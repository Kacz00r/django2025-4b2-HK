from django.http import HttpResponse
 
def landing_page(request):
     return HttpResponse(
         """
         You are on the landing page of polls.app.
         Available urls:
         admin/
         polls/
         """)