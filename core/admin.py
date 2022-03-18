from django.contrib import admin

from core.models import Booking, Destination, Subscription

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Booking)
admin.site.register(Destination)

admin.site.site_header = "Oharlt Sky Jet International"
admin.site.site_title = "Oharlt Sky Jet International"