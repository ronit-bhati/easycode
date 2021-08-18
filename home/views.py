from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# HTML Pages
def home(request):
    allPosts = Post.objects.all().order_by('-views')[:10]
    myPosts = {"post":allPosts}
    return render(request, 'home/home.html', myPosts)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 3 or len(email) < 8 or len(phone) < 10 or len(content) < 5:
            messages.error(request, "Please fill the form correctly!")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your form has been submitted!")
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET.get('query')
    if len(query) > 75:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    params = {"allPosts":allPosts, "query":query}
    if len(allPosts) > 0:
        return render(request, 'home/search.html', params)
    else:
        return render(request, 'home/searchnot.html', params)

# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        # Get Post Parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check Errorneous Inputs
        if len(username) > 15:
            messages.warning(request, "Your Username Can't Have More Than 15 Characters!")
            return redirect('home')

        if pass1 != pass2:
            messages.warning(request, "Your Re-Entered Password Don't Match With Your Password!")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, "Your Username Should Only Contain Lettes And Numbers!")
            return redirect('home')

        if username.lower() != username:
            messages.warning(request, "Your Username Should Be LowerCase Only!")
            return redirect('home')

        # Create The User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your EasyCode account has been successfully created!")
        return redirect('home')

    else:
        return HttpResponse('404 - Forbidden <br><a href="/">Go Home</a>')

def handleLogin(request):
    if request.method == 'POST':
        # Get Post Parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials! Please try again.")
            return redirect('home')
    else:
        return HttpResponse('404 - Forbidden <br><a href="/">Go Home</a>')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('home')
