from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core.views import user
from core.views import content

urlpatterns = [
    path('admin/', admin.site.urls),

    # User API
    path('user/register/', user.RegisterView.as_view()),
    path('user/login/', user.LoginView.as_view()),
    path('user/list/<int:content_id>', user.ListView.as_view()),

    # Content API
    path('content/create/', content.CreateView.as_view()),
    path('content/retrieve/<int:pk>', content.RetrieveView.as_view()),
    path('content/list/', content.ListView.as_view()),
    path('content/share/', content.ShareView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
