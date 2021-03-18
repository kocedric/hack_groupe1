from django.contrib import admin

from .models import Portfolio, Presentation


class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image']}),
        ('Description', {'fields': ['date', 'galerie', 'description']})
    ]
    list_display = ['title', 'date', 'image']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']



class PresentationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'role']}),
        ('Description', {'fields': ['image', 'description', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link']})
    ]
    list_display = ['name', 'role']
    list_filter = ['name', 'role']
    search_fields = ['name', 'role']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Presentation, PresentationAdmin)
# admin.site.register(Portfolio)
