from django.shortcuts import redirect,render
from .forms import CreateUserForm

def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form - CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context={'form':form}
    return render(request,'accounts/signup.html',context)
