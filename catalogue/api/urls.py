#python imports

#django imports
from django.urls import path, include

#third-party imports

#inter-app imports

#local imports


urlpatterns = [
   path('v1/', include('catalogue.api.v1.urls')),
]
