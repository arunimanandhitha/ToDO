from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    task = models.CharField(max_length=255)                     # Task title
    description = models.TextField(blank=True, null=True)       # Optional description
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(blank=True, null=True)          # Optional due date
    is_completed = models.BooleanField(default=False)           # Completion status
    created_at = models.DateTimeField(auto_now_add=True)        # Auto set on creation
    updated_at = models.DateTimeField(auto_now=True)            # Auto set on update

    def __str__(self):
        return self.task

