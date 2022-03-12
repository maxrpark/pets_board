from django.contrib import admin

from .models import Pet, Pet_CV_Comments, FindMe, Find_Me_Comments


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at',)
    # prepopulated_fields = {'slug': ('name', )}


class FindMeAdmin(admin.ModelAdmin):
    list_display = ('name',)

# class FindMeAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    # prepopulated_fields = {'slug': ('name', )}


admin.site.register(Pet, PetAdmin)
admin.site.register(FindMe, FindMeAdmin)
admin.site.register(Pet_CV_Comments)
admin.site.register(Find_Me_Comments)
