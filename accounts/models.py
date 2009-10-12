from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    def is_administrator(self):
        admin_group = Group.objects.get(name="Administrators")
        return admin_group in self.user.groups.all()


def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_user_profile, sender=User)