from django.contrib import admin
from .models import Contact, db_projects, Skills, Adress, Comments

# Register your models here.
admin.site.register(Contact)
admin.site.register(db_projects)
admin.site.register(Skills)
admin.site.register(Adress)
admin.site.register(Comments)
