from django.contrib import admin
from pishing.models import Phish
from pishing.models import FreshPhish
from pishing.models import FixedPhish
from pishing.models import ClonedPhish

# Fresh Phish
class FreshAdmin(admin.ModelAdmin):
    list_display = ('fresh_id', 'fresh_target', )
    list_filter = ('fresh_target',)

# http://stackoverflow.com/questions/12215751/can-i-make-list-filter-in-django-admin-to-only-show-referenced-foreignkeys
class PhishAdmin(admin.ModelAdmin):
    list_display = ('phishyid', 'company',)
    list_filter = ('company',)


class FixedPhishAdmin(admin.ModelAdmin):
    list_display = ('phishyid', 'company',)
    list_filter = ('company',)

class ClonedPhishAdmin(admin.ModelAdmin):
    list_display = ('cloned_phishyid', 'cloned_company', 'cloned_timestamp',)
    list_filter = ('cloned_company',)

# http://stackoverflow.com/a/20413436/1762493
admin.site.register(FreshPhish, FreshAdmin)
admin.site.register(Phish, PhishAdmin)
admin.site.register(FixedPhish, FixedPhishAdmin)
admin.site.register(ClonedPhish, ClonedPhishAdmin)


""" Notes

Customizing Admin CSS / JS
- https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#modeladmin-asset-definitions
- https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#overriding-admin-templates

"""
