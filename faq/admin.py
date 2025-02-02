from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'question_hi', 'question_bn',
                    'question_fr', 'answer_hi', 'answer_bn', 'answer_fr')
    search_fields = ('question', 'language')


admin.site.register(FAQ, FAQAdmin)
