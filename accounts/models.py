from django.db import models


TOP = "top"
SATISFACTORY = "satisfactory"
UNSATISFIED = "unsatisfied"
ACCOUNT_STATUS = (
    (TOP, "top"),
    (SATISFACTORY, "satisfactory"),
    (UNSATISFIED, "unsatisfied"),
)

class Account(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="avtor/")
    bio = models.TextField(max_length=2000)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    
    status = models.CharField(max_length=32, null=True, blank=True, choices=ACCOUNT_STATUS)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.status})"
    