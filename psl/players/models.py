from django.db import models


class Teams(models.Model):
    """
    Database model to add team names
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self)->str:
        return self.name
    
    class Meta:
        verbose_name = 'Teams'
        db_table = 'teams' 
        ordering = ['name']


class Players(models.Model):
    """
    Database model to add players relevant to there teams
    """

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return f"{self.name} ({self.team.name})"
    
    class Meta:
        verbose_name = 'Players'
        db_table = 'players' 
        ordering = ['-created_at']
  

