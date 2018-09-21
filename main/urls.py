from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # /student/<student_id>/
    url(r'^teacher_webpage/$', views.teacher_webpage, name='teacher_webpage'),

    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^student_webpage/$', views.student_webpage, name='student_webpage'),
    url(r'^teacher_webpage/$', views.teacher_webpage, name='teacher_webpage'),
    url(r'^hod_webpage/$', views.hod_webpage, name='hod_webpage'),
    url(r'^caretaker_webpage/$', views.caretaker_webpage, name='caretaker_webpage'),
    url(r'^warden_webpage/$', views.warden_webpage, name='warden_webpage'),
    url(r'^lab1_webpage/$', views.lab1_webpage, name='lab1_webpage'),
    url(r'^cc_webpage/$', views.cc_webpage, name='cc_webpage'),
    url(r'^library_webpage/$', views.library_webpage, name='library_webpage'),
    url(r'^gymkhana_webpage/$', views.gymkhana_webpage, name='gymkhana_webpage'),
    url(r'^onlineCC_webpage/$', views.onlineCC_webpage, name='onlineCC_webpage'),
    url(r'^submitThesis_webpage/$', views.submitThesis_webpage, name='submitThesis_webpage'),
    url(r'^account_webpage/$', views.account_webpage, name='account_webpage'),
    url(r'^assistantRegistrar_webpage/$', views.assistantRegistrar_webpage, name='assistantRegistrar_webpage'),
    # url(r'^(?P<student_id>[0-9]+)/$', views.student_webpage, name='student_webpage'),
    # url(r'^(?P<student_id>[0-9]+)/$', views.student_webpage, name='student_webpage'),

]