from django.contrib import admin
from .models import Feedback  # Import Feedback model

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'feedback_type', 'created_at')  # Show these columns
    search_fields = ('user__username', 'feedback_text')  # Searchable fields
