from django.contrib import admin
from .models import User, Animal, Form, PhoneNumber

# Register your models here.
admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Form)
admin.site.register(PhoneNumber)

