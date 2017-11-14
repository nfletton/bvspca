from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from bvspca.animals.models import Animal


class AnimalModelAdmin(ModelAdmin):
    model = Animal
    menu_label = 'Animals'
    menu_icon = 'fa-paw'
    menu_order = 100
    add_to_settings_menu = False
    list_display = ('title', 'petpoint_id', 'live',)
    search_fields = ('title', 'description', 'petpoint_id')
    list_filter = ('species', 'sex',)
    ordering = ('live', '-petpoint_id',)


modeladmin_register(AnimalModelAdmin)
