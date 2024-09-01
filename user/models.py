from django.db import models

class User(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    PLATFORM_CHOICES = [
        ('TG', 'Telegram'),
        ('BALE', 'Bale'),
    ]
    
    platform = models.CharField(
        max_length=10,
        choices=PLATFORM_CHOICES,
        default='BALE',
    )

    id  = models.CharField(max_length=60, primary_key=True)#models.PositiveBigIntegerField(primary_key  = True)
    user_id = models.PositiveBigIntegerField(null  = True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default = "", blank = True)

    state = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    inviter = models.ForeignKey(
        'user.User',
        related_name='invitee',
        on_delete=models.CASCADE,
        null = True
    )

    class Meta:
        unique_together = ('platform', 'user_id')
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

