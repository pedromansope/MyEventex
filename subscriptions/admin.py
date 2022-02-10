from django.contrib import admin
from django.utils.timezone import now
from subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today',
                    'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ('paid', 'created_at')


    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True #símbolo gráfico se a pessoa inscreveu hoje

admin.site.register(Subscription, SubscriptionModelAdmin)

