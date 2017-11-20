from django.db import models

class Simulator(models.Model):
    simulator_title = models.CharField(max_length=300)

    def __str__(self):
        return self.simulator_title
