from django.contrib import admin
from mainapp.models import Battle, Moves


# Register your models here.
@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Battle._meta.get_fields()]

    # list_filter = ['brand', 'title','release_date','price','status']
    # search_fields = ['brand', 'title','release_date','price','status']


@admin.register(Moves)
class MovesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Moves._meta.get_fields()]
    # list_filter = ['title','status']
    # search_fields = ['title','status']