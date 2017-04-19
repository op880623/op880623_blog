from django.contrib import admin
from .models import Classification, Article


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'     # include a date-based drilldown navigation by that field.
    fieldsets = [
        (None,               {'fields': ['author', 'classification']         }),
        ('content',          {'fields': ['title', 'text', 'source']          }),
        ('Date information', {'fields': [('created_date','published_date')]  }),
    ]
    list_display = ['title', 'author', 'classification', 'created_date', 'published_date']
    list_filter = ['classification', 'created_date', 'author']
    search_fields = ['title', 'text']

admin.site.register(Article, ArticleAdmin)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_classification')

    def parent_classification(self, obj):
        return obj.parent

    parent_classification.empty_value_display = "it's a root classification."

admin.site.register(Classification, ClassificationAdmin)
