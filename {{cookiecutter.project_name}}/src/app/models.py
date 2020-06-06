from copy import copy

from django.db import models


class Model(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, "name"):
            return str(self.name)

        return super().__str__()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def copy(self, **kwargs):
        instance = copy(self)
        instance.update({**kwargs, "pk": None})
        return instance
