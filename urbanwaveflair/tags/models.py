from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type: models.Model, obj_id: int):
        content_type = ContentType.objects.get_for_model(obj_type)
        return self.select_related("tag").filter(
            content_type=content_type, object_id=obj_id
        )


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    objects = TaggedItemManager()
