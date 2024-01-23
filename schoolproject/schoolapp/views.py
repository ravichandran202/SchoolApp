from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AnnouncementForm
from django.contrib.auth import update_session_auth_hash
from .models import StudentDetails,Announcement,Comment,Message,Test,TestMarks,UserQuery
from django.db.models import Q
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.

def account_created_html_email(message):
    subject = 'School App - New Enquiry'
    userquery = message
    context = {
        'userquery' : userquery
    }
    html_message = render_to_string('send-email.html',context=context)
    message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["ravichandrants202@gmail.com",]
    
    send_mail( subject, message, email_from, recipient_list ,html_message=html_message)


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

def home(request):
    user = user_bio = None
    if request.user.is_authenticated:
        user = request.user
        user_bio = StudentDetails.objects.get(user_id = user.id)
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        userquery = UserQuery(username =  name,email= email,phone=phone,description=message)
        userquery.save()
        account_created_html_email(userquery)
        
    return render(request,"home.html",{
        "user":user_bio
    })

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
def create_new_teacher(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        password2 = request.POST['password2']
        full_name = request.POST['full-name']
        roll_num = 0
        stu_class = 0
        date_of_birth = request.POST['dob']
        gender = request.POST['gender']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username Already Exists")
                return redirect('create-teacher')
            elif len(username)<6:
                messages.error(request, "username must contain atleast 6 characters")
                return redirect('create-teacher')
            else:
                user = User.objects.create_user(username, password=password, is_staff = True)
                user.save()
                
                user = User.objects.get(username=username)
                
                student = StudentDetails(user_id = user.id ,student=user,full_name=full_name,roll_no=roll_num,stu_class=stu_class,date_of_birth=date_of_birth,gender=gender)
                student.save()

                messages.info(request, "Account created successfully")
                return redirect('create-teacher')
        else:
            messages.error(request, "Please Enter same Password")
            return redirect('create-teacher')
    return render(request, 'create-teacher-form.html')

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


@login_required(login_url="signin")  
def profile_page(request,id):
    if request.method == 'POST':
        image = request.FILES['profile_image']
        student = StudentDetails.objects.get(id=id)
        
        student.profile_image = image
        student.save()

        
    context = {
        'user':StudentDetails.objects.get(user_id=id)
    }
    return render(request,"profile-page.html",context=context)

@login_required(login_url="signin")
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


@login_required(login_url="signin")
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


@login_required(login_url="signin")
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


@login_required(login_url="signin")
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


@login_required(login_url="signin")
def chat_page(request,id):
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


@login_required(login_url="signin")
def chat(request):
    current_user = request.user
    query = f"select * from schoolapp_StudentDetails inner join schoolapp_Message on schoolapp_StudentDetails.user_id = schoolapp_Message.senderid where schoolapp_Message.senderid = {current_user.id} or schoolapp_Message.receiverid = {current_user.id} or schoolapp_StudentDetails.stu_class=0"
    chat_users = StudentDetails.objects.raw(query)
    chat_users_list = []
    for user in chat_users:
        if user not in chat_users_list and user.user_id != current_user.id:
            chat_users_list.append(user)
    
    if not request.user.is_staff:
        chat_users_list = []
        chat_users = User.objects.filter(is_staff = True)
        for user in chat_users:
            user_bio = StudentDetails.objects.get(user_id = user.id)
            chat_users_list.append(user_bio)

    
    context = {
        "chat_users" : chat_users_list
    }
    return render(request,"chat.html",context=context)

@login_required(login_url="signin")
def users_list(request):
    users = StudentDetails.objects.all().order_by('stu_class').order_by('full_name')
    
    if request.method == 'POST':
        sort_order = request.POST["sort-order"]
        filter_order = request.POST["filter-order"]
        
        if filter_order == 'student':
            users = users.filter(stu_class__gt = 0)
        elif filter_order == 'staff':
            users = users.filter(stu_class__lte = 0)
        elif filter_order == 'all':
            pass
        else:
            users = users.filter(stu_class = filter_order)
        
        
        if sort_order == 'name':
            users = users.order_by("full_name")
        elif sort_order == 'class':
            users = users.order_by("stu_class","full_name")
        elif sort_order == 'gender':
            users = users.order_by("-gender")
    else:
        users = StudentDetails.objects.all().order_by('stu_class').order_by('full_name')
    
    context = {
        'users':users
    }
    return render(request,"display-users.html",context=context)

@login_required(login_url="signin")
def create_test(request):
    if request.method == 'POST':
        title = request.POST['title']
        test_for = request.POST['test_to']
        description = request.POST['description']
        total_marks = request.POST['total-marks'] 
        start_time = request.POST['start_time'] 
        test = Test(title=title,total_marks=total_marks,test_for=test_for,description=description,start_at=start_time)
        test.save()
        students = StudentDetails.objects.exclude(stu_class=0)
        
        if int(test_for) != 0:
            students = StudentDetails.objects.filter(stu_class=test_for)
        
        for student in students:
            TestMarks(test_obj = test, test_id = test.id, student = student ).save()
    return render(request,"create-test.html")

@login_required(login_url="signin")
def display_tests(request):
    tests_list  = Test.objects.all()[::-1]
    if request.method == 'POST':
        filter_order = request.POST["filter-order"]

        if filter_order == 'all':
            tests_list  = Test.objects.all()[::-1]
        else:
            tests_list = Test.objects.filter(test_for = filter_order)[::-1]
        
    else:
        tests_list = Test.objects.all()[::-1]
    
    context = {
        'tests_list' : tests_list
    }
    return render(request,"display-tests.html",context=context)

@login_required(login_url="signin")
def delete_test(request,id):
    test_obj = Test.objects.filter(id=id)
    try:
        test_obj.delete()
    except:
        pass
    return redirect("display_tests")

@login_required(login_url="signin")
def upload_marks(request,id):
    test_marks_list = TestMarks.objects.filter(test_id=id)
    
    context = {
        'test_marks_list' : test_marks_list
    }
    return render(request,"upload-marks.html",context=context)

def set_grade(score):
    print(score)
    if score>=90:
        return "A+"
    elif score>=80 and score<90:
        return "A"
    elif score>=65 and score<80:
        return "B"
    elif score>=35 and score<65:
        return "C"
    else:
        return "F"

@login_required(login_url="signin")
def update_marks(request,id):
    student_test_marks = TestMarks.objects.get(id=id)
    if request.method == 'POST':
        kannada_marks = request.POST['kannada_marks']
        english_marks = request.POST['english_marks']
        hindi_marks = request.POST['hindi_marks']
        science_marks = request.POST['science_marks']
        maths_marks = request.POST['maths_marks']
        social_marks = request.POST['social_marks']
        
        student_test_marks.kannada = kannada_marks
        student_test_marks.english = english_marks
        student_test_marks.hindi = hindi_marks
        student_test_marks.science = science_marks
        student_test_marks.maths = maths_marks
        student_test_marks.social = social_marks
        total_score = float(kannada_marks)+float(english_marks)+float(hindi_marks)+float(science_marks)+float(maths_marks)+float(social_marks)
        student_test_marks.total_scored_marks = total_score
        student_test_marks.total_marks = student_test_marks.test_obj.total_marks*6
        grade_percentage = int((total_score / (student_test_marks.test_obj.total_marks*6))*100)
        student_test_marks.grade = set_grade(grade_percentage)
        passing_marks = (35 / 100) * student_test_marks.test_obj.total_marks
        marks_list = [kannada_marks,english_marks,hindi_marks,science_marks,maths_marks,social_marks]
        is_pass = True
        for subject_marks in marks_list:
            if float(subject_marks)<passing_marks:
                is_pass = False
        
        student_test_marks.is_pass = is_pass
        student_test_marks.save()
        
    return redirect("upload_marks",student_test_marks.test_id)


def is_ready(model_time):
    date_time = str(model_time)[:18]
    date_object = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    if (date_object <= datetime.now()):
        return True
    return False
    
@login_required(login_url="signin")
def student_display_tests(request):
    user = request.user
    student = StudentDetails.objects.get(user_id = user.id)
    tests_list = TestMarks.objects.filter(student = student)
    
    for test in tests_list:
        test_obj = test.test_obj
        if is_ready(test_obj.start_at):
            test_obj.is_ready = True
        else:
            test_obj.is_ready = False
        test_obj.save()
    
    context = {
        "tests_list" : tests_list.order_by('created_at')[::-1]
    }
    return render(request,"student-display-tests.html",context=context)

@login_required(login_url="signin")
def marks_card(request,id):
    test = TestMarks.objects.get(id=id)
    context = {
        "test":test
    }
    return render(request,"marks-card.html",context=context)