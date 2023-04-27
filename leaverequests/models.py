from django.db import models
from django.conf import settings

class LeaveRequest(models.Model):
    PENDING = 1
    APPROVED = 2
    DENIED = 3

    STATUS_FIELD = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (DENIED, "Denied")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="leave_requests")
    from_date = models.DateField()
    to_date = models.DateField()
    from_hour = models.TimeField(blank=True, null=True)
    to_hour = models.TimeField(blank=True, null=True)
    details = models.TextField(blank=True, max_length=150)
    status = models.PositiveSmallIntegerField(choices=STATUS_FIELD, default=1)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="reviewer", blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)

    def __str__(self):
        status_dict = dict(self.STATUS_FIELD)
        return f"{self.user}: {status_dict[self.status]}"