from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import*
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q, Count



def main(request):
    post = Post.objects.order_by('-post_date')[:4]
    mostlike =  Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:4]
    mostlike1 =  Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:1]
    context = {'post':post, 'mostlike':mostlike , 'mostlike1':mostlike1}
    return render(request, 'main.html', context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def home(request):
    post = Post.objects.all()
    prov = Province.objects.all()
    mostlike =  Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:4]
  
    company_contains_query = request.GET.get('company_contains')
    position_contains_query = request.GET.get('position_contains')
    id_exact_query = request.GET.get('id_exact')
    intern_type = request.GET.get('intern_type')
    money_min = request.GET.get('money_min')
    money_max = request.GET.get('money_max')
    money_type = request.GET.get('money_type')
    rating = request.GET.get('rating')
    

    if is_valid_queryparam(company_contains_query):
        post = post.filter(title__icontains=company_contains_query)

    if is_valid_queryparam(position_contains_query):
        post = post.filter(position__icontains=position_contains_query)
    
    if is_valid_queryparam(money_min):
        post = post.filter(money__gte=money_min)

    if is_valid_queryparam(money_max):
        post = post.filter(money__lt=money_max)

    if is_valid_queryparam(money_type) and money_type != 'เลือก...':
        post = post.filter(money_type=money_type)

    if is_valid_queryparam(id_exact_query) and id_exact_query != 'เลือก...':
        post = post.filter(prov=id_exact_query)

    if is_valid_queryparam(intern_type) and intern_type != 'เลือก...':
        post = post.filter(Intern_type=intern_type)
    
    if is_valid_queryparam(rating) and rating != 'เลือก...':
        post = post.filter(rating=rating)

    page = request.GET.get("page")
    paginator = Paginator(post, 8)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post': post, 
        'mostlike': mostlike,
        'prov': prov,
        }

    return render(request, 'home.html', context)

def addpost(request):
    userId = request.user.profile.id
    user = Profile.objects.get(id=userId)
    prov_name = Province.objects.all()
    context = {'prov_name':prov_name}
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        prov_id = data.get('prov')
        prov = Province.objects.get(id=prov_id)
        location = data.get('location')
        location2 = data.get('location2')
        location3 = data.get('location3')
        location4 = data.get('location4')
        position = data.get('position')
        Intern_type = data.get('Intern_type')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        money = data.get('money')
        money_type = data.get('money_type')
        introduce = data.get('introduce')
        body = data.get('body')
        body2 = data.get('body2')
        body3 = data.get('body3')
        body4 = data.get('body4')
        body5 = data.get('body5')
        rating = data.get('rating')
        imageTitles = data.getlist('imageTitle')
        images = request.FILES.getlist('image')

        newPost = Post()
        newPost.title = title
        newPost.prov = prov
        newPost.location = location
        newPost.location2 = location2
        newPost.location3 = location3
        newPost.location4 = location4
        newPost.position = position
        newPost.Intern_type = Intern_type
        newPost.start_time = start_time
        newPost.end_time = end_time
        newPost.money = money
        newPost.money_type = money_type
        newPost.introduce = introduce
        newPost.body = body
        newPost.body2 = body2
        newPost.body3 = body3
        newPost.body4 = body4
        newPost.body5 = body5
        newPost.rating = rating

        document1 = request.FILES['document1']
        document2 = request.FILES['document2']
        document3 = request.FILES['document3']
        document4 = request.FILES['document4']
        newPost.document1 = document1
        newPost.document2 = document2
        newPost.document3 = document3
        newPost.document4 = document4

        newPost.createBy = user
        ###Save Image###
        file_thumbnail = request.FILES['thumbnail']
        newPost.thumbnail = file_thumbnail
        ################

        newPost.save()

        if imageTitles and images:
                for image, imageTitle in zip(images, imageTitles):
                    if imageTitle != "":
                        new_otherPostImage = otherPostImage()
                        new_otherPostImage.post  = Post.objects.get(title=title)
                        new_otherPostImage.image = image
                        new_otherPostImage.image_name = imageTitle
                        new_otherPostImage.save()

        messages.success(request,'เพื่มเนื้อหาเสร็จสิ้น รอทางผู้ดูแลอนุมัติเนื้อหาดังกล่าว')
        return redirect('update-post', newPost.id)

    return render(request, 'add_post.html', context)

def postdetail(request,id):
    try:
        user = request.user.profile.id
        userId = Profile.objects.get(id=user)
        postdetail = Post.objects.filter(id=id)
        my_internWorks = internWorks.objects.filter(post=id)
        my_otherPostImage = otherPostImage.objects.filter(post=id)
        comment = Comment.objects.filter(post=id)
        myBookmark = Bookmark.objects.filter(bookmark = id, user = user)
        post = get_object_or_404(Post, id=id)
        my_otherPostImageCount = my_otherPostImage.count()
        commentCount = comment.count()

        is_liked = False
        if post.likes.filter(id=request.user.profile.id).exists():
            is_liked = True

    except:
        postdetail = Post.objects.filter(id=id)
        my_internWorks = internWorks.objects.filter(post=id)
        my_otherPostImage = otherPostImage.objects.filter(post=id)
        comment = Comment.objects.filter(post=id)
        my_otherPostImageCount = my_otherPostImage.count()
        commentCount = comment.count()
        myBookmark = Bookmark.objects.filter(bookmark = id)
        is_liked = False

    if request.user.profile.id != post.createBy.id and post.active == False and request.user.profile.usertype != 'admin':
        return redirect('home')

    if request.method == 'POST':
        data = request.POST.copy()
        comment = data.get('comment')

        if data.get('comment') if 'comment' in request.POST else None:
            newComment = Comment()
            newComment.user = userId
            newComment.comment = comment
            newComment.post = post
            newComment.save()

        return redirect(request.META['HTTP_REFERER'])
    
    context = {
        'postdetail':postdetail,
        'my_internWorks':my_internWorks,
        'my_otherPostImage':my_otherPostImage,
        'my_otherPostImageCount':my_otherPostImageCount,
        'comment':comment,
        'commentCount':commentCount,
        'myBookmark':myBookmark,
        'is_liked':is_liked,
    }

    return render(request, 'article_details.html', context)

def like_post(request):
    try:
        username = request.user.profile.username
    except:
        return redirect('/login/')
        
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    is_liked = False
    if post.likes.filter(id=request.user.profile.id).exists():
        post.likes.remove(request.user.profile.id)
        is_liked = False
    else:
        post.likes.add(request.user.profile.id)
        is_liked = True
    
    return HttpResponseRedirect(post.get_absolute_url())

def updatepost(request,id):
    post = Post.objects.get(id=id)
    image = otherPostImage.objects.filter(post=id)
    work = internWorks.objects.filter(post=id)
    prov_name = Province.objects.all()
    context = {'prov_name':prov_name,'post':post,'image':image, 'work':work}

    if request.user.profile.id != post.createBy.id:
        return redirect('/home')


    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        prov_id = data.get('prov')
        prov = Province.objects.get(id=prov_id)
        location = data.get('location')
        location2 = data.get('location2')
        location3 = data.get('location3')
        location4 = data.get('location4')
        position = data.get('position')
        Intern_type = data.get('Intern_type')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        money = data.get('money')
        money_type = data.get('money_type')
        introduce = data.get('introduce')
        body = data.get('body')
        body2 = data.get('body2')
        body3 = data.get('body3')
        body4 = data.get('body4')
        body5 = data.get('body5')
        rating = data.get('rating')
        imageTitles = data.getlist('imageTitle')
        images = request.FILES.getlist('image')

        editPost = Post.objects.get(id=id)
        editPost.title = title
        editPost.prov = prov
        editPost.location = location
        editPost.location2 = location2
        editPost.location3 = location3
        editPost.location4 = location4
        editPost.position = position
        editPost.Intern_type = Intern_type
        editPost.start_time = start_time
        editPost.end_time = end_time
        editPost.money = money
        editPost.money_type = money_type
        editPost.introduce = introduce
        editPost.body = body
        editPost.body2 = body2
        editPost.body3 = body3
        editPost.body4 = body4
        editPost.body5 = body5
        editPost.rating = rating

        document1 = request.FILES['document1']
        document2 = request.FILES['document2']
        document3 = request.FILES['document3']
        document4 = request.FILES['document4']
        editPost.document1 = document1
        editPost.document2 = document2
        editPost.document3 = document3
        editPost.document4 = document4

        editPost.save()
        ###Save Image###

        for image, imageTitle in zip(images, imageTitles):
            if imageTitle != "":
                new_otherPostImage = otherPostImage()
                new_otherPostImage.post  = Post.objects.get(title=title)
                new_otherPostImage.image = image
                new_otherPostImage.image_name = imageTitle
                new_otherPostImage.save()

        if "thumbnail" in request.FILES:
            editPost_thumbnail = request.FILES['thumbnail']
            editPost.thumbnail = editPost_thumbnail
            editPost.save()

        check1 = request.POST.getlist('check1[]')
        print(check1)
        for i in check1:
            a = otherPostImage.objects.get(pk=i)
            a.delete()

        check2 = request.POST.getlist('check2[]')
        print(check2)
        for x in check2:
            b = internWorks.objects.get(pk=x)
            b.delete()

        messages.success(request,'อัพเดตเนื้อหาเสร็จสิ้น')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect('article-detail', id)

    return render(request, 'update_post.html', context)

def edit_otherPostImage(request,id,iid):
    pid = request.GET.get('id', id)
    other = otherPostImage.objects.get(id=iid)
    
    if request.user.profile.id != other.post.createBy.id:
        return redirect('/home')

    if request.method == 'POST':
        data = request.POST.copy()
        image_name = data.get('image_name')
            
        edit_otherPostImage = otherPostImage.objects.get(id=iid)
        edit_otherPostImage.image_name = image_name
        edit_otherPostImage.save()
        ###Save Image###

        if "image" in request.FILES:
            edit_otherPostImage_image = request.FILES['image']
            edit_otherPostImage.image = edit_otherPostImage_image
            edit_otherPostImage.save()

        messages.success(request,'แก้ไขรูปภาพเพิ่มเติมเสร็จสิ้น')
        return redirect('edit-otherPostImage', id, iid)

    context = {'pid':pid,'other':other}
    return render(request, 'edit-otherPostImage.html',context)

def delete_otherPostImage(request,id,iid):
    pid = request.GET.get('id', id)
    other = otherPostImage.objects.get(id=iid)
    other.delete()

    return redirect('update-post', pid)

def delete_internWorks(request,id,wid):
    pid = request.GET.get('id', id)
    work = otherPostImage.objects.get(id=wid)
    work.delete()

    return redirect('update-post', pid)
    
def deletepost(request,id):
    post = Post.objects.get(id=id)
    context = {'post':post}

    if request.user.profile.id != post.createBy.id:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', context)

def profile(request, username):
    currentUser = request.user.profile.username
    url = request.GET.get('username', username)
    user = Profile.objects.all()
    post = Post.objects.all()
    # userId = request.user.profile.id
    # post = Post.objects.filter(createBy = userId).order_by('id').reverse()

    context = {
        'currentUser' : currentUser,
        'url' : url,
        'profile' : user,
        'post' : post
        
    }

    return render(request, 'profile.html', context)

def profile_edit(request, username):
    currentUser = request.user.username
    url = request.GET.get('username', username)
    user = Profile.objects.all()
    context = {
        'currentUser' : currentUser,
        'url' : url,
        'profile' : user
    }
    data = Profile.objects.get(user__id=request.user.id)
    context["data"]=data
    if request.method == "POST":
        # new_user_name = request.POST["user_name"]
        new_first_name = request.POST["first_name"]
        new_last_name = request.POST["last_name"]
        new_email = request.POST["email"]
        new_bio = request.POST["bio"]
        new_tel = request.POST["tel"]
        new_facebook = request.POST["facebook"]
        new_twitter = request.POST["twitter"]
        new_instagram = request.POST["instagram"]
        new_website = request.POST["website"]
        new_github = request.POST["github"]

        user = User.objects.get(id=request.user.id)
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.email = new_email
        user.save()

        # data.username = new_user_name
        data.bio = new_bio
        data.tel = new_tel
        data.facebook = new_facebook
        data.twitter = new_twitter
        data.instagram = new_instagram
        data.website = new_website
        data.github = new_github
        data.save()

        if "photo" in request.FILES:
            new_photo = request.FILES["photo"]
            data.photo = new_photo
            data.save()

        # context["status"] = "อัพเดตโปรไฟล์เสร็จสิ้น"
        messages.success(request,'อัพเดตโปรไฟล์เสร็จสิ้น')
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'profile_edit.html', context)

def profile_post(request):
    userId = request.user.profile.id
    post = Post.objects.filter(createBy = userId).order_by('id').reverse()
    
    context = {'post':post}
    return render(request, 'profile_post.html', context)

def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        user_name = data.get('user_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email):
            messages.warning(request,'Email นี้ถูกใช้ไปแล้ว')
            return redirect('/register/')

        elif User.objects.filter(username=user_name):
            messages.warning(request,'ชื่อผู้ใช้ นี้ถูกใช้ไปแล้ว')
            return redirect('/register/')
            
        else:
            newuser = User()
            newuser.username = user_name
            newuser.email = email
            newuser.first_name = first_name
            newuser.last_name = last_name
            newuser.set_password(password)
            newuser.save()

            # profile = Profile()
            # profile.username = user_name
            # profile.user = User.objects.get(username=email)
            # profile.save()
            
            profile = Profile()
            profile.user = User.objects.get(username=user_name)
            profile.username = user_name
            profile.save()

            messages.success(request,'สมัครสมาชิกเสร็จสิ้น')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        login(request, user)
        
    return render(request, 'register.html')

def addBookmark(request,id):
    try:
        username = request.user.profile.username
        user = Profile.objects.get(username=username)
        post = Post.objects.get(id=id)
    except:
        return redirect('/login/')

    
    if Bookmark.objects.filter(user=user,bookmarkId=id):
        delete_bookmark = Bookmark.objects.filter(user=user,bookmarkId=id)
        delete_bookmark.delete()
        messages.info(request,'ลบบันทึกเรียบร้อย')
        
    else:
        newbookmark = Bookmark()
        newbookmark.user = user
        newbookmark.bookmarkId = id
        newbookmark.bookmark = post
        newbookmark.save()
        messages.info(request,'เพิ่มเข้าบันทึกเรียบร้อย')
    
    return redirect(request.META['HTTP_REFERER'])

def myBookmark(request):
    username = request.user.profile.username
    user = Profile.objects.get(username=username)
    mybookmark = Bookmark.objects.filter(user=user)
    context = {'mybookmark':mybookmark}
    return render(request,'profile_bookmark.html',context)

def delete_bookmark(request,id):
    bookmark = Bookmark.objects.get(id=id)
    bookmark.delete()
    messages.success(request,'ลบบันทึกดังกล่าวเสร็จสิ้น')
    return redirect(request.META['HTTP_REFERER'])

def delete_comment(request, id):  
    comment = Comment.objects.get(id=id)  
    comment.delete() 
    messages.success(request,'ลบความคิดเห็นดังกล่าวเสร็จสิ้น')
    return redirect(request.META['HTTP_REFERER'])

def delete_post(request, id):  
    post =Post.objects.get(id=id)  
    post.delete() 
    messages.success(request,'ลบเนื้อหาดังกล่าวเสร็จสิ้น')
    return redirect(request.META['HTTP_REFERER'])

def edit_comment(request,id,cid):
    pid = request.GET.get('id', id)
    comment = Comment.objects.get(id=cid)
    
    if request.user.profile.id != comment.user.id:
        return redirect('/home')

    if request.method == 'POST':
        data = request.POST.copy()
        comment = data.get('comment')
            
        edit_comment = Comment.objects.get(id=cid)
        edit_comment.comment = comment
        edit_comment.save()

        messages.success(request,'แก้ไขความคิดเห็นเสร็จสิ้น')
        return redirect('edit-comment', id, cid)

    context = {'pid':pid,'comment':comment}
    return render(request, 'edit-comment.html',context)
#----------------------------------- ADMIN ----------------------------------

def admin_member (request):
    if request.user.profile.usertype != 'admin':
        return redirect('home')

    profile = Profile.objects.all()
    context = {'profile':profile}

    return render(request, 'admin_member.html', context)

def admin_confirm (request):
    if request.user.profile.usertype != 'admin':
        return redirect('home')

    post = Post.objects.all()
    context = {'post':post}
    return render(request, 'admin_confirm.html', context)

def admin_post(request):
    if request.user.profile.usertype != 'admin':
        return redirect('home')

    post = Post.objects.all()
    context = {'post':post}

    if request.method == 'POST':
        check = request.POST.getlist('check1[]')
        print(check)
        for p in check:
            b = Post.objects.get(pk=p)
            b.delete()

        messages.success(request,'ลบเนื้อหาเสร็จสิ้น')
        # return redirect(request.META['HTTP_REFERER'])
        return redirect('admin-post')
        
    return render(request, 'admin_post.html', context)

def admin_delete_post(request, id):  
    post = Post.objects.get(id=id)  
    post.delete() 
    messages.success(request,'ลบเนื้อหาเสร็จสิ้น')
    return redirect('admin-post')

def admin_delete_member(request, id):  
    profile = Profile.objects.get(id=id)  
    user = User.objects.get(username=profile)  
    user.delete() 
    messages.success(request,'ลบสมาชิกเสร็จสิ้น')
    return redirect('admin-member')

def updatePostStatus (request, id, status):
        if request.user.profile.usertype != 'admin':
            return redirect('home')

        post = Post.objects.get(id=id)
        if status == 'active':
            post.active = True
            post.save()
            return redirect ('admin-confirm')
        elif status == 'inactive':
            post.active = False
            post.save()
            return redirect ('admin-post')
        
        
def studentRegister (request):
    username = request.user.profile.username
    user = Profile.objects.get(username=username)
    
    if request.method == 'POST':
        data = request.POST.copy()
        identificationNumber = data.get('identificationNumber')
        studentCard = request.FILES["studentCard"]

        newStudent = StudentPending()
        newStudent.user = user
        newStudent.studentCard = studentCard
        newStudent.identificationNumber = identificationNumber
        newStudent.save()

        user = Profile.objects.get(username=username)
        user.apply = True
        user.save()

        
        messages.success(request,'ส่งหลักฐานยืนยันความเป็นนักศึกษาเรียบร้อย รอทางแอดมินตรวจสอบ')
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'student-register.html')
    
def updateStudentStatus (request, uid, tid, status):
    if request.user.profile.userType != 'admin':
        return redirect('home')
        
    StudentPending = StudentPending.objects.get(id=tid)
    profile = Profile.objects.get(id=uid)
    
    if status == 'approve':
        StudentPending.approve = True
        profile.userType = 'teacher'
        StudentPending.save()
    elif status == 'disapprove':
        StudentPending.approve = False
        profile.userType = 'student'
        profile.apply = False
        StudentPending.delete()
        
    profile.save()

    return redirect ('teacher')
    
def admin_studentPending (request):
    student = StudentPending.objects.all()
    
    context = {
		'student' : student
	}
    
    return render(request, 'admin_studentPending.html', context)