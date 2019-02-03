from django.db import models
from django.contrib.auth.models import User
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    namee = models.CharField(max_length=200)

    can_rock = models.BooleanField(default=True)

    nam = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
            ('g', "Guitar"),
            ('b', "Bass"),
            ('d', "Drums"),
        ),
        max_length=1
    )
    # band = models.ForeignKey("Band",on_delete=models.CASCADE)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Band(models.Model):
    """A model of a rock band."""
    namek = models.CharField(max_length=200)
    can_rockk = models.BooleanField(default=True)
