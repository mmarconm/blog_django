from django.db.models.signals import (
    pre_save
)

from django.dispatch import receiver
from articles.models import Article
from django.utils.text import slugify

@receiver(pre_save, sender=Article)
def add_slug_to_article(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        instance.slug = slugify(instance.title)