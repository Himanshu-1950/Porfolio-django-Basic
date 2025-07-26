from django.db import models
from django.utils.translation import gettext_lazy as _  # optional but recommended

class Home(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    role1 = models.CharField(max_length=50)
    role2 = models.CharField(_("Role 2"), max_length=50)

    def __str__(self) -> str:
        return self.name
