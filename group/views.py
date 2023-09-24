from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .form import EditGroupForm,NewGroupForm

from .models import Group

def groups(request):

    groups = Group.objects.all().order_by('-weight')


    return render(request, 'group/groups.html',{
        'groups': groups,

    })



@login_required
def detail(request, pk):
    group = get_object_or_404(Group, pk=pk, created_by=request.user)

    return render(request, 'group/detail.html', {
        'group': group
    })



@login_required
def new_group(request):
    
    if request.method == 'POST':
        form = NewGroupForm(request.POST)

        if form.is_valid():
            group = form.save(commit=False)
            group.user = request.user
            group.created_by = request.user
            group.save()
        
            return redirect('group:detail', pk=group.id)
    else:
        form = NewGroupForm()

    return render(request, 'group/form.html',{
        'form': form,
        'title': 'New Group',
    })

# pk = primary key
@login_required
def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditGroupForm(request.POST, instance=group)

        if form.is_valid():
            form.save()

            return redirect('/groups', pk=group.id)
        
    else:
        form = EditGroupForm(instance=group)

    return render(request, 'group/form.html',{
        'form': form,
        'title': 'Edit group',
    })

@login_required
def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk, created_by=request.user)
    group.delete()

    return redirect('group:groups')
