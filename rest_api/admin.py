from django.contrib import admin
from .models import Produto, Foto

from rest_framework.authtoken.admin import TokenAdmin

class SiteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    #list_filter = ('email') https://www.youtube.com/watch?v=SKo2B8Vf53M
    search_fields = ('first_name', 'last_name', 'email')

TokenAdmin.raw_id_fields = ('user',)

admin.site.site_header = "Produto Administração"
admin.site.index_title = "Administração"
admin.site.site_title = "Administração"

# Register your models here.
# admin.site.register(Bucketlist)
admin.site.register(Produto, SiteAdmin)
admin.site.register(Foto)

# @admin.register(Produto)
# class AuthorAdmin(admin.ModelAdmin):
#   date_hierarchy = 'created'
#   search_fields = ['first_name', 'last_name', 'email']
#   list_display = ('first_name','last_name','email')
#   list_filter = ('status',)

#   admin.site.register(models.Author, AuthorAdmin)
