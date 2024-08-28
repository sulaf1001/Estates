from django.contrib import admin
from .models import Property

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'num_beds', 'num_baths', 'squarft', 'contact_num', 'description', 'price','image','image1','image2', 'approved')
    list_filter = ('approved',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Property, PropertyAdmin)

