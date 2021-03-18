from django.contrib import admin

from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image']}),
        ('Description', {'fields': ['date', 'description']})
    ]
    list_display = ['title', 'date', 'image']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


admin.site.register(Portfolio, PortfolioAdmin)
# admin.site.register(Portfolio)
