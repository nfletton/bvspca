from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import SocialMediaQueue


class NewsSocialMediaQueueModelAdmin(ModelAdmin):
    model = SocialMediaQueue
    menu_label = 'SM Queue'
    menu_icon = 'fa-share-square '
    menu_order = 450
    add_to_settings_menu = True
    list_display = ('date', 'priority', '__str__', 'ready')
    ordering = ('priority', 'date')
    list_per_page = 20


modeladmin_register(NewsSocialMediaQueueModelAdmin)
