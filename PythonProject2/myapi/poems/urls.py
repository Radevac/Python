from django.urls import path
from .views import (get_random_poem, get_poem_by_author, get_poem_by_theme,
                    get_all_authors, get_all_themes, get_titles_by_author, get_titles_by_theme,
                    create_author, create_theme, create_poem, update_poem, delete_poem)

urlpatterns = [
    path('poem/random/', get_random_poem),
    path('poem/author/', get_poem_by_author),
    path('poem/theme/', get_poem_by_theme),
    path('poem/authors/', get_all_authors),
    path('poem/themes/', get_all_themes),
    path('poem/titles/author/', get_titles_by_author),
    path('poem/titles/theme/', get_titles_by_theme),


    path('poem/create/', create_poem),
    path('poem/update/<int:poem_id>/', update_poem),
    path('poem/delete/<int:poem_id>/', delete_poem),

    path('author/create/', create_author),
    path('theme/create/', create_theme),
]
