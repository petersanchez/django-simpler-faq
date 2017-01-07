#! coding: utf-8
from django.contrib import admin
from .models import Topic, Question


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'number')
    list_editable = ('number',)


class QuestionAdmin(FAQAdmin):
    list_filter = ('topic',)


admin.site.register(Topic, FAQAdmin)
admin.site.register(Question, QuestionAdmin)
