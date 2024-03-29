from django.urls import path, include
from .views import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', main, name = 'main'),
    path('home/', home, name="home"),
    path('add_post/', login_required(addpost, login_url='login'), name="add-post"),

    path('article/<int:id>', login_required(postdetail, login_url='login'), name="article-detail"),

    path('article/edit/<int:id>/', updatepost, name="update-post"),

    path('article/edit/<int:id>/delete-otherPostImage/<int:iid>/', delete_otherPostImage, name="delete-otherPostImage"),
    path('article/edit/<int:id>/delete-internWorks/<int:wid>/', delete_internWorks, name="delete-internWorkse"),

    path('article/edit/<int:id>/edit-otherPostImage/<int:iid>/', edit_otherPostImage, name='edit-otherPostImage'),

    path('article/<int:id>/remove', deletepost , name="delete-post"),
    path('register/', register, name="register"),
    path('profile/<str:username>', login_required(profile, login_url='login'), name="profile"),
    path('profile/<str:username>/edit', login_required(profile_edit, login_url='login'), name="profile-edit"),
    path('profile_post', login_required(profile_post, login_url='login'), name="profile-post"),
    path('addbookmark/<int:id>', addBookmark, name="add-bookmark"),
    path('profile_bookmark', login_required(myBookmark, login_url='login'), name="profile-bookmark"),

    path('admin_post', login_required(admin_post, login_url='login'), name="admin-post"),
    path('admin-delete-post/<int:id>/', login_required(admin_delete_post, login_url='login'), name="admin-delete-post"),
    path('admin-delete-memberApprove/<int:id>/', login_required(admin_delete_memberApprove, login_url='login'), name="admin-delete-member"),

    path('admin_confirm', login_required(admin_confirm, login_url='login'), name="admin-confirm"),

    path('admin_member', login_required(admin_member, login_url='login'), name="admin-member"),

    path('admin_student_confirmed', login_required(admin_student_confirmed, login_url='login'), name="admin-student-confirmed"),

    path(r'^like/$', like_post, name="like_post"),

    path('update-post-status/<int:id>/<str:status>', updatePostStatus, name='updatePostStatus'),

    path('article/<int:id>/edit-comment/<int:cid>/', login_required(edit_comment, login_url='login'), name="edit-comment"),
    path('delete-comment/<int:id>/', login_required(delete_comment, login_url='login'), name="delete-comment"),
    path('delete-post/<int:id>/', login_required(delete_post, login_url='login'), name="delete-post"),
    path('delete-bookmark/<int:id>/', login_required(delete_bookmark, login_url='login'), name="delete-bookmark"),

    path('student-register', login_required(studentRegister, login_url='login'), name='student-register'),


    path('admin_studentPending', admin_studentPending, name='admin-studentPending'),
    path('admin_update-student-status/<int:uid>/<int:sid>/<str:status>', updateStudentStatus, name='updateStudentStatus'),

    
]