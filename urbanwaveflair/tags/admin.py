from django.contrib import admin

from urbanwaveflair.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["label"]
