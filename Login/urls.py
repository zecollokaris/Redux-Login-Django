"""Login URL Configuration"""

from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static

# Imports Views For Success to Render Content.
from Success import views

'''Here we have imported (include)-: this allows us to add the Success url pattern
as done below this is to avoid filling up all our urls in this page'''

''' End Of Import'''
#-------------------------------#


urlpatterns = [
    path('admin/', admin.site.urls),
    # Includes Success url patterns
    path('', include('Success.urls')),
]
