from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    FEEDBACK_TYPES = (
        ('translation', 'Translation Quality'),
        ('ui', 'User Interface'),
        ('feature', 'Feature Request'),
        ('bug', 'Bug Report'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)    
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_feedback_type_display()} feedback by {self.user.username}"
