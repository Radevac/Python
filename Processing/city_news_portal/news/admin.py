from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Article, Comment, Tag, SiteSettings, BannedUser

#  Автоматично створюємо групу "Адміністратор"
def create_admin_group():
    group, created = Group.objects.get_or_create(name='Адміністратор')
    if created:
        print("✅ Групу 'Адміністратор' створено!")

create_admin_group()

#  Додаємо адміністратора в групу (якщо існує)
try:
    admin_user = User.objects.get(username='admin')
    admin_group = Group.objects.get(name='Адміністратор')
    admin_user.groups.add(admin_group)
except User.DoesNotExist:
    print("⚠️ Користувач 'admin' ще не створений.")
except Group.DoesNotExist:
    print("⚠️ Група 'Адміністратор' ще не існує.")

#  Налаштування панелі адміністрування для статей
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'content')
    list_filter = ('date_published', 'author', 'tags')
    ordering = ['-date_published']

#  Налаштування панелі адміністрування для коментарів
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'text', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('text',)

#  Налаштування панелі адміністрування для блокування користувачів
class BannedUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'banned_until')
    search_fields = ('user__username',)

# Реєструємо моделі в Django Admin
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(SiteSettings)
admin.site.register(BannedUser, BannedUserAdmin)
