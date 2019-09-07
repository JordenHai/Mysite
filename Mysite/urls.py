"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
urlpatterns = [
    path('app01/', include("app01.urls")),
    path('app02/', include("app02.urls")),
]

#url的分发系统
"""
path('admin/', admin.site.urls),
#re_path('index/(\d+)/', views.index, name='indexx'),
re_path('index/(?P<nid>\d+)/(?P<uid>\d+)', views.index, name='indexx'),
# path('indefsdfsdgshgsfdhgfdhjgfdx/', views.index,name='indexx'),
path('login/', views.login),
path('dumps/', views.loadfile),
path('home/',  views.Home.as_view()),
#re_path(r'detail-(\d+).html', views.detail),  # 动态路由系统
#re_path(r'detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),  # 动态路由系统
re_path(r'detail-(?P<nid>\d+).html', views.detail),  # 动态路由系统
"""