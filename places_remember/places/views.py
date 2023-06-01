from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from places_remember.forms import MemoryForm
from .models import Memory


def index(request):
    """
    Начальная страница.
    """
    return render(request, 'index.html')


@login_required
def home(request):
    """
    Страница пользователя.
    """
    user = request.user
    profile_picture = None
    memories = Memory.objects.filter(user=user)

    if user.is_authenticated and user.socialaccount_set.filter(
        provider='vk'
    ).exists():
        vk_provider = user.socialaccount_set.get(provider='vk')
        profile_picture = vk_provider.extra_data.get('photo_max_orig')

    context = {
        'user': user,
        'profile_picture': profile_picture,
        'memories': memories,
    }
    return render(request, 'home.html', context)


@login_required
def add_memory(request):
    """
    Страница добавленя места.
    """
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            memory = form.save(commit=False)
            memory.latitude = latitude
            memory.longitude = longitude
            memory.name = name
            memory.comment = comment
            memory.user = request.user
            memory.save()

            return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'add_memory.html', {'form': form})


@login_required
def display_memory(request, memory_id):
    """
    Страница отображения места пользователя.
    """
    memory = get_object_or_404(Memory, id=memory_id)

    if request.method == 'POST':
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemoryForm(instance=memory)

    context = {'memory': memory, 'form': form}
    return render(request, 'display_memory.html', context)
