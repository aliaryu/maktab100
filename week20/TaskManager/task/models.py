from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(verbose_name="Category", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(verbose_name="Tag", max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag


def date_validation(value):
    if value < timezone.now().date():
        raise ValidationError("Please enter a future date sheytun balaw.")


STATUS_CHOICES = [
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]


class Task(models.Model):
    title       = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description")
    due_date    = models.DateField(verbose_name="Due Date", validators=[date_validation])
    status      = models.CharField(
        verbose_name="Status",
        max_length=1,
        choices=STATUS_CHOICES,
        default="I"
    )
    user     = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        models.CASCADE,
        verbose_name="Category",
        related_name="tasks"
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Tags",
        related_name="tasks"
    )

    class Meta:
        ordering = ["-due_date"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title
