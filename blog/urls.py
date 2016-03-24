from django.conf.urls import url
# from django.contrib import admin

import blog.core.views

urlpatterns = [
#     url(r'^admin/', admin.site.urls),
    url(r'^$', blog.core.views.index),
    url(r'^(?P<slug>[a-z-]+)/', blog.core.views.slug),
]
