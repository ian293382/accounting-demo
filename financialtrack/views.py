from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .form import NewFinancialRecordForm, EditFinancialRecordForm, NewTagForm, EditTagForm

from.models import Tag, FinancialRecord

from group.models import Group

@login_required
def new_tag(request, group_id):
    group = get_object_or_404(Group, pk=group_id, created_by=request.user)

    if request.method == 'POST':
        form = NewTagForm(request.POST)

        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.save()
            return redirect('group:detail', pk=group_id)  # 重定向到特定群组的详细页面

    else:
        form = NewTagForm()

    return render(request, 'financialtrack:new_tag.html', {
        'group': group,
        'form': form,
    })
        
@login_required
def edit_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditTagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            return redirect('group:detail', pk=tag.group.pk)  # 使用tag的group属性

    else:
        form = EditTagForm(instance=tag)

    return render(request, 'financialtrack/form.html', {
        'form': form,
        'title': 'Edit Tag',
    })

@login_required
def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk, created_by=request.user)
    tag.delete()

    return redirect('groups:detail')


@login_required
def new_financial_record(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'POST':
        form = NewFinancialRecordForm(request.POST)

        if form.is_valid():
            financial_record = form.save(commit=False)
            financial_record.group = group
            financial_record.save()
        return redirect('group:detail', group_id=group_id)
    
    else:    
        form = NewFinancialRecordForm()

    return render(request, 'financialtrack/new_record.html',{
        'group': group,
        'form': form,
    })

@login_required
def edit_financial_record(request, group_id, record_pk):
    group = Group.objects.get(pk=group_id)
    financial_record = get_object_or_404(FinancialRecord, record_pk=FinancialRecord.id, group=group)

    if request.method == 'POST':
        form = EditFinancialRecordForm(request.POST, instance=financial_record)

        if form.is_valid():
          
            financial_record.save()
        return redirect('group:detail', group_id=group_id)
    
    else:    
        form = EditFinancialRecordForm(instance=financial_record)

    return render(request, 'financialtrack/new_record.html',{
        'group': group,
        'form': form,
        'financial_record': financial_record,
    })

@login_required
def delete_financial_record(group_id, financialrecord_id):
    group = Group.objects.get(pk=group_id)
    financial_record = get_object_or_404(FinancialRecord, pk=financialrecord_id, group=group)

    financial_record.delete()

    return redirect('group:detail', pk=group_id)