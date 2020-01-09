from django.db import models


class Plant(models.Model):

    quantity = models.IntegerField(blank=True, null=True)
    # do I need the id from the external DB

    # foreign key
    # do i need a related name?-- something to keep in mind
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("plant")
        verbose_name_plural = _("plants")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plant_detail", kwargs={"pk": self.pk})
