from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/',null=True)

    def __str__(self):
     return self.title
 
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    @classmethod
    def location(cls):
        news = cls.objects.all()
        return news
    @classmethod
    def search_by_cat(cls, search_term):
        news=cls.objects.filter(category__icontains=search_term)
        return news

class Category(models.Model):
    name = models.CharField(max_length =30, null=True)

    def __str__(self):
        return self.name
    def save_Category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name