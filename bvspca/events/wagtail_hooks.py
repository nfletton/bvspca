from wagtail_modeladmin.helpers import PagePermissionHelper
from wagtail_modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Event


class EventsPagePermissionHelper(PagePermissionHelper):
    def user_can_list(self, user):
        """
        Only show news list page in admin if user can create one
        """
        return self.user_can_create(user)


class EventModelAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'
    menu_icon = 'date'
    menu_order = 105
    add_to_settings_menu = False
    list_display = ('title', 'start_date', 'end_date',)
    ordering = ('-start_date',)
    list_per_page = 20
    permission_helper_class = EventsPagePermissionHelper


modeladmin_register(EventModelAdmin)
