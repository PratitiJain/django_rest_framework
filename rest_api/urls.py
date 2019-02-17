from django.conf.urls import url

from rest_api.views import AlbumAPI

app_name = 'rest_api'

urlpatterns = [
    url(r'^albums/', AlbumAPI.as_view(), name="album-api")
]
