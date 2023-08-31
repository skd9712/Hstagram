from django.db import models

class Feed(models.Model):
    content = models.TextField() # 글내용
    image = models.TextField() # 피드 이미지
    profile_image = models.TextField() # 프로필 이미지
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    user_id = models.TextField() # 글쓴이
    like_count = models.IntegerField() # 좋아요 수

class Reply(models.Model):
    feed_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=30,blank=True,null=True)
    content = models.TextField()
    email = models.EmailField(verbose_name='email',max_length=100,blank=True,null=True)

    class Meta:
        indexes = [
            models.Index(fields=['feed_id'])
        ]
class FeedLike(models.Model):
    feed_id = models.IntegerField()
    email = models.CharField(max_length=30,blank=True,null=True)
    is_like = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['feed_id']),
            models.Index(fields=['email']),
        ]

class Bookmark(models.Model):
    email = models.EmailField(verbose_name='email',max_length=100)
    feed_id = models.IntegerField()
    is_bookmarked = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['email'])
        ]