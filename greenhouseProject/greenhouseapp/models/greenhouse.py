from django.db import models


class Greenhouse(models.Model):
    title = models.CharField(max_length=50)

    # foreign keys

    # related name?-- something to keep in mind
    greenhousetype = models.ForeignKey(
        GreenhouseType, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("greenhouse")
        verbose_name_plural = _("greenhouses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("greenhouse_detail", kwargs={"pk": self.pk})
