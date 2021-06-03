from django.contrib import admin

# Register your models here.

from .models import Daily, Evaluation
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Evaluation)
admin.site.register(Daily, MarkdownxModelAdmin)
