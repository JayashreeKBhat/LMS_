from django.contrib import admin
from .models import *


# Register your models here.

class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn


class requirements_TabularInline(admin.TabularInline):
    model = Requirements


class video_TabularInline(admin.TabularInline):
    model = Video

class quiz_TabularInline(admin.TabularInline):
    model = Quiz


class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline, requirements_TabularInline, video_TabularInline, quiz_TabularInline)



admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Level)
admin.site.register(LearnOut)
admin.site.register(What_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Language)

admin.site.register(UserCourse)
admin.site.register(QuesModel)

