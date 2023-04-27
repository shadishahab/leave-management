from django.db import models
#from people.models import Person

class Company(models.Model):
    name =models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

    @classmethod
    def get_company(cls, company_id):
        company = cls.objects.get(pk=company_id)
        return company

class Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class ConfirmationCode(models.Model):
    from people.models import Person

    value = models.IntegerField(unique=True, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="confirmation_codes")
    is_used = models.BooleanField(default=False)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="validation_code", blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Confirmation Code'
        verbose_name_plural = 'Confirmation Codes'
        
    def __str__(self):
        return f"{self.value}"

