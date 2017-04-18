from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Classification(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True)

    def list_child(self):
        return Classification.objects.filter(parent=self)

    def list_offspring(self):
        offspring = self.list_child()
        for child in self.list_child():
            offspring = offspring.union(child.list_offspring())
        return offspring

    def list_content(self):
        return Article.objects.filter(classification=self)

    def list_all_content(self):
        all_content = self.list_content()
        for child in self.list_child():
            all_content = all_content.union(child.list_all_content())
        return all_content

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    classification = models.ForeignKey(Classification, blank=True, null=True)
    source = models.URLField(max_length=200)

    def slug(self):
        return slugify(self.title, allow_unicode=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def list_sibling(self):
        return self.classification.list_content()

    def __str__(self):
        return self.title
