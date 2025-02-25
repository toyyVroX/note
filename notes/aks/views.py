from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

@login_required
def note_list(request):

    if request.method == 'POST' and "form_izi" in request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('aks:note_list')
    else:
        form = NoteForm()

    if request.method == 'POST' and 'delete_note' in request.POST:
        print("работає")
        note_id = request.POST.get('delete_note')
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return redirect('aks:note_list')

    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'form': form, 'notes': notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})
    

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('aks:note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('aks:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})