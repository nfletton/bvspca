from wagtail_modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import SocialMediaQueue


class NewsSocialMediaQueueModelAdmin(ModelAdmin):
    model = SocialMediaQueue
    menu_label = 'SM Queue'
    menu_icon = 'fa-share-square '
    menu_order = 450
    add_to_settings_menu = True
    list_display = ('date', 'priority', 'page_link', 'status')
    ordering = ('priority', 'date')
    list_per_page = 20


modeladmin_register(NewsSocialMediaQueueModelAdmin)
