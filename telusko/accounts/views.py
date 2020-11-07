from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect("accounts:register")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("accounts:register")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")

                return redirect("accounts:login")

        else:
            messages.info(request, "Passwords don't match")
            return redirect("accounts:register")

        # return redirect("/")
    else:
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "Invalid credentials")
            return redirect("accounts:login")

    else:
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")


@login_required()
def logout(request):
    auth.logout(request)
    return redirect("/")
