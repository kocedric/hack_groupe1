from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    fields = [
        (None, {'fields': ['title', 'image']}),
        ('Description', {'fields': ['date', 'description']})
    ]
    list_display = ('title', 'date')
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


admin.site.register(Portfolio, PortfolioAdmin)
