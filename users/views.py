from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, render_to_response

#Sign up form
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to Log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    #user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        #u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if(p_form.is_valid()):
            #u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        #u_form =UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        #'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def like_post(request, userId):
    user = get_object_or_404(User, pk=userId)
    user.profile.numLikes = user.profile.numLikes + 1
    user.profile.save()

    context = {
        'user': user,
    }
    return render(request, 'users/noEditProfile.html', context)
    
@login_required
def dislike_post(request, userId):
    user = get_object_or_404(User, pk=userId)

    if user.profile.numLikes != 0:
        user.profile.numLikes = user.profile.numLikes - 1
        user.profile.save()

    context = {
        'user': user,
    }
    return render(request, 'users/noEditProfile.html', context)