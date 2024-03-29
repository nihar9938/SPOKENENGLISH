from django.contrib import admin
from Main.models import *
# Register your models here.

class AdminNews(admin.ModelAdmin):
    list_display = ('id','title', 'valid')
    
    class Meta(object):
        ordering = ('valid',)

admin.site.register(News, AdminNews)

class AdminRegister(admin.ModelAdmin):
    list_display = ('Name','Email','Phone','Course')

admin.site.register(Register,AdminRegister)

class AdminMail(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Mail,AdminMail)


class AdminCourses(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Courses, AdminCourses)

class AdminReview(admin.ModelAdmin):
    list_display = ('name', 'review', 'type')

admin.site.register(Review, AdminReview)
