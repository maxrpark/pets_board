from django.db import models
from django.utils.text import slugify
import datetime as dt

# from django.db.models.signals import pre_delete
# import cloudinary
# @receiver(pre_delete, sender=image)
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)


class Pet(models.Model):

    #  sex choices
    NO = 'no'
    Yes = 'yes'

    CHOICES_STATUS = (
        (NO, 'No'),
        (Yes, 'Yes')
    )
    #  sex choices
    FEMALE = 'female'
    MALE = 'male'

    CHOICES_SEX = (
        (FEMALE, 'Female'),
        (MALE, 'Male')
    )

    #  size choices
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'
    REALLY_BIG = 'really big'

    CHOICES_SIZE = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (BIG, 'Big'),
        (REALLY_BIG, 'Really Big')
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pets_cv/', null=True)
    age = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=10, choices=CHOICES_SEX, default=NO)
    neutered = models.CharField(
        max_length=10, choices=CHOICES_STATUS, default=NO)
    size = models.CharField(
        max_length=10, choices=CHOICES_SIZE, default=NO)
    about_me = models.TextField(max_length=250)
    skills = models.TextField(max_length=250)
    achievements = models.TextField(max_length=250)
    things_I_like = models.TextField(max_length=250)
    things_Dont_like = models.TextField(max_length=250)
    desire_compensation = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True, editable=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    slug = models.SlugField(default='', null=False, editable=False)

    def save(self, *args, **kwargs):
        now = dt.datetime.now()
        self.slug = slugify(
            self.name + "-" + now.strftime('%Y-%m-%d %H-%M-%S.-%f')[:-3])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Pet_CV_Comments(models.Model):
    pet_cv = models.ForeignKey(
        Pet, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name


class FindMe(models.Model):
    #  sex choices
    NO = 'no'
    Yes = 'yes'

    CHOICES_STATUS = (
        (NO, 'No'),
        (Yes, 'Yes')
    )
    #  sex choices
    FEMALE = 'female'
    MALE = 'male'

    CHOICES_SEX = (
        (FEMALE, 'Female'),
        (MALE, 'Male')
    )

    #  size choices
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'
    REALLY_BIG = 'really big'

    CHOICES_SIZE = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (BIG, 'Big'),
        (REALLY_BIG, 'Really Big')
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pets_find_me/', null=True)
    age = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=10, choices=CHOICES_SEX, default=NO)
    neutered = models.CharField(
        max_length=10, choices=CHOICES_STATUS, default=NO)
    size = models.CharField(
        max_length=10, choices=CHOICES_SIZE, default=NO)
    about_me = models.TextField(max_length=250)
    create_at = models.DateTimeField(
        auto_now_add=True, editable=True, null=True,)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    slug = models.SlugField(default='', null=False, editable=False)

    class Meta:
        verbose_name_plural = 'Find Me'

    def save(self, *args, **kwargs):
        now = dt.datetime.now()
        self.slug = slugify(
            self.name + "-" + now.strftime('%Y-%m-%d %H-%M-%S.-%f')[:-3])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Find_Me_Comments(models.Model):
    pet_find_me = models.ForeignKey(
        FindMe, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name
