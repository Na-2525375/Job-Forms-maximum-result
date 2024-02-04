
from django.contrib import admin
from myApp.models import *


class customUser_Display(admin.ModelAdmin):

    list_display=['username']


admin.site.register(customUser)
admin.site.register(jobApplyModel)
admin.site.register(addJobModel)


