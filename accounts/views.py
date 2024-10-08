from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """REgister a new user"""
    if request.method != 'POST':
        #Display a blank registration form
        form = UserCreationForm()
    else:
        # Process complete form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log new user in and redirect them to homepage
            login(request, new_user)
            return redirect('learning_logs:index')
        
    #Display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

