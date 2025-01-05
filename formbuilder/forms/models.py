from django.db import models
from django.core.exceptions import ValidationError


def validate_order(value):
    if value < 1:
        raise ValidationError("Order must be greater than zero.")



class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Field(models.Model):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    FIELD_TYPES = [
        (TEXT, 'Text'),
        (NUMBER, 'Number'),
        (DATE, 'Date'),
    ]

    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='fields',  null=True, blank=True)
    label = models.CharField(max_length=100, default='Default Label')
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES, default='text')
    required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(validators=[validate_order])

    def __str__(self):
        return f"{self.label} ({self.field_type})"

class Submission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)