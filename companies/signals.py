from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, ConfirmationCode
from .utils import random_code_generator
from django.utils import timezone

@receiver(post_save, sender=Company)
def create_confirmation_codes(sender, instance, created, **kwargs):
    if created:
        codes = random_code_generator(10)
        for i in range(10):
            ConfirmationCode.objects.create(company=instance, value=codes[i], creation=timezone.now())