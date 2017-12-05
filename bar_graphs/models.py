from django.db import models


class Bar_graph(models.Model):
    bgraph_title = models.CharField(max_length=200)

    def __str__(self):
        return self.bgraph_title
