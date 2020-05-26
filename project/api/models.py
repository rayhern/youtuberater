from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    author = models.TextField(max_length=50)

    def rating_average(self):
        rating_sum = 0
        ratings = Rating.objects.filter(video=self)
        for rating in ratings:
            rating_sum += rating.stars
        if len(ratings) > 0:
            return rating_sum // len(ratings)
        else:
            return 0

    def comments_list(self):
        all_comments = Rating.objects.filter(video=self)
        listallcomments = []
        for comment in all_comments:
            listallcomments.append('<b>%s</b> - %s' % (comment.user.username, comment.comments))
        return listallcomments

    def __str__(self):
        return self.url


class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = ('user', 'video')
        index_together = ('user', 'video')
