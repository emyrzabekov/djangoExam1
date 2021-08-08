from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

