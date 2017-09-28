from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photo_posts')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='NoImage.jpg')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def save(self, *args, **kwargs):
        is_duplicated = False

        if self.photo:
            try:
                before_obj = Photo.objects.get(id=self.id)
                if before_obj.photo == self.photo:
                    is_duplicated = True
            except:
                pass
        if is_duplicated:
            image_obj = Image.open(self.photo).convert("L")
            new_image_io = BytesIO
            image_obj.save(new_image_io, format='JPEG')

            temp_name = self.photo.name
            self.photo.delete(save=False)

            self.photo.save(
                temp_name,
                content = ContentFile(new_image_io.getValue()),
                save= False
            )
            try:
                before_obj = Photo.objects.get(id=self.id)
                if before_obj.photo == self.photo or is_duplicated:
                    self.photo = before_obj.photo
                else :
                    before_obj.photo.delete(save=False)

            except:
                pass
        super(Photo, self).save(*args,**kwargs)
@receiver(post_delete, sender=Photo)
def post_delete(sender, instance, **kwargs):
    storage,path = instance.photo.storage, instance.photo.path
    if (path != '.') and (path!='/') and (path!='photos/')and(path!='photos/.'):
        storage.delete(path)