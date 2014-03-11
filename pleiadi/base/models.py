from django.db import models


class BaseModel(models.Model):
    """
    Pleiadi base model
    """

    class Meta:
        abstract = True
