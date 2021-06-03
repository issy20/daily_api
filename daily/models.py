from django.db import models

# Create your models here.

from markdownx.models import MarkdownxField


class Daily(models.Model):
    date = models.DateField()
    input = MarkdownxField()
    output = MarkdownxField()
    question = MarkdownxField()
    other = MarkdownxField()
    summary = MarkdownxField()
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT)
    isOpen = models.BooleanField(default=True)

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str


class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation
