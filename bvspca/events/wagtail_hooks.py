from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Event


class EventModelAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'
    menu_icon = 'date'
    menu_order = 470
    add_to_settings_menu = False
    list_display = ('title', 'start_date',)
    ordering = ('-start_date',)


modeladmin_register(EventModelAdmin)
