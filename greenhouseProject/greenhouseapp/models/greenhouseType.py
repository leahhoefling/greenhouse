from django.db import models


class GreenhouseType(models.Model):

    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("greenhouseType")
        verbose_name_plural = _("greenhouseTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("greenhouseType_detail", kwargs={"pk": self.pk})
