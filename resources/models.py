from django.db import models

class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Genre(DateTimeModel):
    """Model representing a movie genre"""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Director(DateTimeModel):
    """Model representing a movie director"""
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=1000, default="")
    country = models.CharField(max_length=150, default="")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Actor(DateTimeModel):
    """Model representing a movie actor"""
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=1000, default="")
    country = models.CharField(max_length=150, default="")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Movie(DateTimeModel):
    """Movie model"""
    title = models.CharField(max_length=250)
    synopsis = models.TextField(max_length=1000, help_text='Synopsis of the movie')
    cover = models.CharField(max_length=500, default="")
    trailer = models.CharField(max_length=500, default="")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True, related_name="movies")
    cast = models.ManyToManyField(Actor, help_text='Select the actors of this movie', related_name="movies")
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this game')
    release_date = models.DateField(null=True, blank=True)
    running_time = models.CharField(max_length=500, default="")
    country = models.CharField(max_length=300, default="")
    language = models.CharField(max_length=500, default="")
    magnet = models.CharField(max_length=1000, default="")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Screenshot(DateTimeModel):
    """Model representing a movie screenshot"""
    url = models.CharField(max_length=1000, default="")
    movie = models.ForeignKey(Movie, related_name='screenshots', on_delete=models.CASCADE)