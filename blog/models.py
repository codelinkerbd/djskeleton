from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class BlogCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Category Title"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug/URL"), default=get_random_string(8))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Category Title"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug/URL"), default=get_random_string(8))
    primary_category = models.ForeignKey(BlogCategory, null=True, blank=True, on_delete=models.SET_NULL,
                                         verbose_name=_("Category"))
    summary = models.TextField(null=True, blank=True, verbose_name=_("Summary"))
    details = models.TextField(null=True, blank=True, verbose_name=_("Details"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")