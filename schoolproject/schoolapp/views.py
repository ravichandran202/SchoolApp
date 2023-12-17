from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AnnouncementForm
from django.contrib.auth import update_session_auth_hash
from .models import StudentDetails,Announcement,Comment,Message
from django.db.models import Q
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect("signin")

    return render(request, "signin.html")

@login_required(login_url="signin")
def home(request):
    return render(request,"home.html")

@login_required(login_url="signin")
def create_new_user(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        password2 = request.POST['password2']
        full_name = request.POST['full-name']
        roll_num = request.POST['rollnum']
        stu_class = request.POST['class']
        date_of_birth = request.POST['dob']
        gender = request.POST['gender']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username Already Exists")
                return redirect('create-user')
            elif len(username)<6:
                messages.error(request, "username must contain atleast 6 characters")
                return redirect('create-user')
            else:
                user = User.objects.create_user(username, password=password)
                user.save()
                
                user = User.objects.get(username=username)
                
                student = StudentDetails(user_id = user.id ,student=user,full_name=full_name,roll_no=roll_num,stu_class=stu_class,date_of_birth=date_of_birth,gender=gender)
                student.save()

                messages.info(request, "Account created successfully")
                return redirect('create-user')
        else:
            messages.error(request, "Please Enter same Password")
            return redirect('create-user')
    return render(request, 'create-user-form.html')

@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url="signin")

def edit_student_profile(request,id):
    if request.method == 'POST':
        # image = None
        # try:
        #     image = request.FILES['profile_image']
        # except:
        #     pass
        email = request.POST['stu_email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip-code']
        father_name =  request.POST['father_name']
        father_number =  request.POST['father_number']
        mother_name =  request.POST['mother_name']
        mother_number =  request.POST['mother_number']
        
        student = StudentDetails.objects.get(id=id)
        
        # student.profile_image = image
        student.email = email
        student.street = street
        student.city = city
        student.state = state
        student.zip_code = zip_code
        student.father_name = father_name
        student.father_contact = father_number
        student.mother_name = mother_name
        student.mother_contact = mother_number
        
        student.save()
        context = {
        'user':StudentDetails.objects.get(id=id)
        }
        return redirect("profile_page",student.id)
    
    user = None
    try:
        user = StudentDetails.objects.get(id=id)
    except:
        return HttpResponse("Error Occured")
    
    context = {
        'user':user
    }
    
    return render(request, 'edit-student-details.html',context=context)

@login_required(login_url="signin")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })


    
def profile_page(request,id):
    if request.method == 'POST':
        image = request.FILES['profile_image']
        student = StudentDetails.objects.get(id=id)
        
        student.profile_image = image
        student.save()
        
    context = {
        'user':StudentDetails.objects.get(id=id)
    }
    return render(request,"profile-page.html",context=context)

def create_announchment(request):
    if request.method == 'POST':
        image = None
        title = request.POST['title']
        try:
            image = request.FILES['image_file']
        except:
            image = None
        content = request.POST['content']
        announce_to = request.POST['announce_to']
        
        Announcement(created_by = request.user, title=title,image=image,content=content,announce_to=announce_to).save()
        
    return render(request,"create-announcement.html")

def edit_announchment(request,id):
    form_model = Announcement.objects.get(id=id)
    form = AnnouncementForm(instance= form_model)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST,instance= form_model)
        if form.is_valid():
            form.save()
    else:
        form = AnnouncementForm(instance= form_model)
    context = {
        'form':form
    }
    return render(request,"edit-announcement.html",context=context) 


from django.db.models import Count

def announcements(request):
    result = Announcement.objects.all()
    user_id = request.user.id  #get current userid
    student_details = StudentDetails.objects.get(user_id = user_id) #Get Student details 
    student_class = student_details.stu_class #get student class
    
    #filter the announcements according to Student
    announcements = Announcement.objects.raw(f"select * from schoolapp_announcement where announce_to = 0 or announce_to =  {student_class}")
    
    # if the user is staff get all announcements
    if request.user.is_staff: 
        announcements = Announcement.objects.all()
        
    context = {
        'announcements':announcements[::-1]
    }
    return render(request,"announcements.html",context) 

def announcement(request,id):
    announcement = Announcement.objects.get(id=id)
    if request.method == 'POST':
        content = request.POST['content']
        new_comment = Comment(created_by = request.user, content = content, announcement_post = announcement)
        new_comment.save()
        
    comments = Comment.objects.filter(announcement_post = announcement)[::-1]

    context = {
        'announcement':announcement,
        'comments':comments
    }
    return render(request,"announcement-page.html",context) 

def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    announcement = comment.announcement_post
    comment.delete()
    return redirect("announchment",announcement.id)

def chat(request,id):
    sender = request.user
    receiver = User.objects.get(id=id)
    receiver_bio = StudentDetails.objects.get(user_id = receiver.id)
    sender_bio = StudentDetails.objects.get(user_id = sender.id)
    
    
    if request.method == 'POST':
        content = request.POST['content']
        Message(sender=sender, receiver=receiver, senderid=sender.id, receiverid = receiver.id , content=content).save()
    
    messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
    messages = messages.order_by('created_at')
    # messages = Message.objects.filter( ( Q(sender=sender) & Q(receiver=receiver)  ) | ( Q(sender=receiver) & Q(receiver=sender) )).order_by('created_at')
    
    
    context = {
        "sender":sender,
        "receiver_bio" : receiver_bio,
        "sender_bio" : sender_bio,
        "messages" : messages
    }
    
    return render(request,"chatting-page.html",context=context)