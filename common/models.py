from coin.ftns import influ
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    계정과 연동되는 모델
    이메일, 선호 암호화폐 및 인플루언서 저장
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    namelist = models.CharField(max_length=200)

    influencer_list = tuple((i, j) for i, j in zip(influ, influ))

    influencers = models.CharField(max_length=500, choices=influencer_list)

    # 사용자 계정 생성 및 저장 시 동시에 저장
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
