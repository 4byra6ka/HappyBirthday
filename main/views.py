from django.shortcuts import render


def main_view(request):
    """Контроллер главной страницы"""
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'main/main.html', context)
