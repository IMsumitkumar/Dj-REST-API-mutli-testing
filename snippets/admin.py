from django.contrib import admin

# Register your models here.
from .models import Snippet, Blog, Task

# making reead only fields 

# class SnippetAdmin(admin.ModelAdmin):
#     readonly_fields = ('highlighted',)
# admin.site.register(Snippet, SnippetAdmin)

admin.site.register(Snippet)
admin.site.register(Blog)
admin.site.register(Task)
