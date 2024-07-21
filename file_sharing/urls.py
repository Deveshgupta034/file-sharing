from django.urls import path
from .views import UserSignupView, FileUploadView, FileListView, FileDownloadView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDownloadView.as_view(), name='file-download'),
]