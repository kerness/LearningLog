from django.db import models

# Create your models here.

class Topic(models.Model):
    """ A topic the user is learning about. """
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """ Return a string representation of the model. """
        return self.text

class Entry(models.Model):
    """ Something specific learned about a topic. """
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # when topic is deleted - all entries associated with topic should be deleted as well. ALSO: connect with specified topic by ForeginKey
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries' # without this, Django would refer to multiple entries as Entrys

    def __str__(self): # define infomration to show - only first 50 characters of text
        """ Return a string representation of the model. """
        if len(self.text) > 50:
            strRepresentation = f"{self.text[:50]}..."
        else:
            strRepresentation = self.text
        return strRepresentation
        