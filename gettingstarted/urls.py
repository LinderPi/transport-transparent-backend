from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path("blog/", blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # path("",  name=""),
    path("about/", hello.views.about, name="about"),
    path("calculator/", hello.views.calculator, name="calculator"),
    path("companies/", hello.views.companies, name="companies"),
    path("company/<int:pk>/", hello.views.company, name="company"),

    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
]
