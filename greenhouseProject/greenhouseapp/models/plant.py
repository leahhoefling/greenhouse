from django.db import models


class Plant(models.Model):

    quantity = models.CharField(max_length=50)
    # do I need the id from the external DB and the greenhouse FK?

    class Meta:
        verbose_name = _("plant")
        verbose_name_plural = _("plants")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plant_detail", kwargs={"pk": self.pk})
