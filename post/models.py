from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericRelation

from django.db.models import Sum

from django.contrib.postgres.fields import ArrayField

from django.utils import timezone


class LikeManager(models.Manager):
    use_for_related_fields = True

    # def likes(self):
    #     return self.get_queryset().filter(vote__gt=0)
    #
    # def dislikes(self):
    #     return self.get_queryset().filter(vote__lt=0)



    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def posts(self):
        return self.get_queryset().filter(content_type__model='post').order_by('-posts__pub_date')

    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')


class LikePost(models.Model):
    # LIKE = 1
    # DISLIKE = -1
    #
    # VOTES = ((DISLIKE, 'Не нравится'),(LIKE, 'Нравится'))
    # vote = models.SmallIntegerField(verbose_name=("Голос"), choices=VOTES)

    like = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likepost', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.SmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.like)

    # objects = LikeManager()

    def like_(self):
        self.like = not (self.like)

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    like = GenericRelation(LikePost, related_query_name='posts')
    auhtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def total_like(self):
        return self.like.filter(like=True).count()

class Comment(models.Model):
    path = ArrayField(models.IntegerField())
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pud_date = models.DateTimeField(auto_now_add=True)
    like = GenericRelation(LikePost, related_query_name='comments')

    def __str__(self):
        return self.text

    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:level = 5
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 5:level = 5
        return 12 - level
