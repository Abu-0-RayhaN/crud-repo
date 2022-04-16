from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import userpost
from .forms import customerform
#creating postdate
def create(request):
    form= customerform()
    if request.method=='POST':
        Form=customerform(request.POST)
        if Form.is_valid():
            Form.save()
    Form={}
    context ={'form':form}
    return render(request,'create.html',context)
#reading the post
def read(request):
    user_data=userpost.objects.all()
    context ={ 'user_data':user_data}
    return render(request,'read.html',context)
#Updating the post
def update(request,pk):
    get_user_data=get_object_or_404(userpost,pk=pk)
    form= customerform(instance=get_user_data)
    if request.method=='POST':
        form=customerform(request.POST,instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request,'User data has been Updated')
            return redirect('read')
    return render(request,'update.html',context={'form':form})
# alternative
# def update(request,pk):
#     get_user_data = get_object_or_404(userpost,pk=pk)
#     if request.method=='POST':
#         #         ↓ work with a form
#         form = UserPostForm(request.POST, request.FILES, instance=get_user_data)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'User data has been Updated')
#             return redirect('read')
#     else:
#         #         ↓ work with a form
#         form= UserPostForm(instance=get_user_data)
#     context={'form':form}
#     return render(request,'update.html',context)

#deleting the post
def delete(request,pk):
    get_user=get_object_or_404(userpost,pk=pk)
    get_user.delete()
    messages.error(request,'User deleted')
    return redirect('/')