from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^passwordreset/$',views.passwordreset,name='passwordreset'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^user_detials/(?P<pk>\d+)$',views.userdetials,name='userdetials'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
