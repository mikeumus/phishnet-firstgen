from django.contrib import admin
from pishing.models import Phish
from pishing.models import FixedPhish
from pishing.models import ClonedPhish

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
admin.site.register(Phish, PhishAdmin)
admin.site.register(FixedPhish, FixedPhishAdmin)
admin.site.register(ClonedPhish, ClonedPhishAdmin)