from django.contrib import admin

from .models import Question, Choice

#admin.StackedInline was used before tabular (tab justs condenses the view)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #allows u to reorganize how the things show order
    inlines = [ChoiceInline]
    # gives u '3' choices for each question
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # gives filter on right side
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
