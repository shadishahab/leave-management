from celery import shared_task
from .models import Company, ConfirmationCode
from .utils import random_code_generator

@shared_task
def up_to_ten():
    companies = Company.objects.all()
    for company in companies:
        unused_codes = company.validation_codes.filter(is_used=False)
        if unused_codes.count() < 10:
            n = 10 - unused_codes.count()
            codes = random_code_generator(n)
            for i in range(n):
                ConfirmationCode.objects.create(company=company, value=codes[i])