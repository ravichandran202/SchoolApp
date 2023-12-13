from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import StudentDetails
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
                
                student = StudentDetails(student=user,full_name=full_name,roll_no=roll_num,stu_class=stu_class,date_of_birth=date_of_birth,gender=gender)
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
        image = request.FILES['profile_image']
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
        
        student.profile_image = image
        student.email = email
        student.street = street
        student.city = city
        student.state = state
        student.zip_code = zip_code
        student.father_name = father_name
        student.father_contact = father_number
        student.mother_name = mother_name
        student.mother_contact = mother_number
        
        user = student.save()
        update_session_auth_hash(request, user)
        
    user = None
    try:
        user = StudentDetails.objects.get(id=id)
        print()
    except:
        return HttpResponse("Error Occured")
    
    context = {
        'user':user
    }
    
    return render(request, 'edit-student-details.html',context=context)

@login_required(login_url="signin")
def change_password(request):
    user = User.objects.get(id=15)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
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


    
