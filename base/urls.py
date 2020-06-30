from django.urls import path
from . import views
from base.views import Agents,AgentListView, AgentInfo, AgentUpdateView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='base-home'),
	path('register', views.register, name='register'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/agent_details/', AgentListView.as_view(), name='agent-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/agent/', AgentInfo.as_view(), name='agent-info'),
    path('users/', Agents.as_view(), name='agents'),
    path('post/agent/<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update-time'),
]
