from django.db import models
from companies.models import Role, Company
from django.conf import settings

class Person(models.Model):        
    MALE = 1
    FEMALE = 2

    GENDER_FIELD = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="person")
    gender = models.PositiveSmallIntegerField(blank=True, null=True, choices=GENDER_FIELD)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="employees")
    phone_no = models.CharField(max_length=11)
    job_title = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="jobholders")
    is_employer = models.BooleanField(default=False)
    balance = models.FloatField(default=208) #(hours)

    class Meta:
        verbose_name_plural = "People"
        
    def __str__(self):
        return str(self.user)
