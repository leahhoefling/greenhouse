from django.db import models


class Greenhouse(models.Model):
    title = models.CharField(max_length=50)

    # do I need foreign keys of user and type here?

    class Meta:
        verbose_name = _("greenhouse")
        verbose_name_plural = _("greenhouses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("greenhouse_detail", kwargs={"pk": self.pk})
