from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='ticket_image', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])
