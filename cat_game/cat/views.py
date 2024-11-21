from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat

def set_name(request):
    cat = Cat.objects.first()
    if cat and cat.name:
        return redirect('cat_info')

    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            cat = Cat.objects.create(name=name)
            return redirect('cat_info')

    return render(request, 'cat/set_name.html')

def stop_game(request, cat_id):
    """Представление для прекращения игры"""
    cat = get_object_or_404(Cat, id=cat_id)  # Получаем кота по ID
    cat.stop_playing()  # Вызываем метод stop_playing
    return redirect('cat_detail', cat_id=cat.id)

def cat_info(request):
    cat = Cat.objects.first()
    if not cat:
        return redirect('set_name')

    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "feed":
            cat.feed()
        elif action == "play":
            cat.play()
        elif action == "stop_playing":
            cat.stop_playing()
        elif action == "sleep":
            cat.sleep()

        return redirect('cat_info')

    return render(request, 'cat/cat_info.html', {'cat': cat})
