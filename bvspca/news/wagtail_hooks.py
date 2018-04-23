from wagtail.contrib.modeladmin.helpers import PagePermissionHelper
from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)


from .models import News


class NewsPagePermissionHelper(PagePermissionHelper):
    def user_can_list(self, user):
        """
        Only show news list page in admin if user can create one
        """
        return self.user_can_create(user)


class NewsModelAdmin(ModelAdmin):
    model = News
    menu_label = 'News'
    menu_icon = 'date'
    menu_order = 110
    add_to_settings_menu = False
    list_display = ('title', 'first_published_at',)
    ordering = ('-first_published_at',)
    list_per_page = 20
    permission_helper_class = NewsPagePermissionHelper


modeladmin_register(NewsModelAdmin)
