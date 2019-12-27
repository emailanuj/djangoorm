from django.contrib import admin

# Register your models here.
from .models import Publication,Article,Reporter,News,Place,Restaurant

admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(News)
admin.site.register(Place)
admin.site.register(Restaurant)