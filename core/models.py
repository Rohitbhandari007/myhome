from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LightningScenes(models.Model):
    """
    Model representing the lightning scenes.

    Attributes:
        name (str): The name of the lightning scene.
        color (str): The color of the lightning scene in hexadecimal format.
        brightness (int): The brightness level of the lightning scene.
    """
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default='#ffffff')

    def __str__(self):
        return self.name
            

class Home(TimeStampedModel):
    """
    Represents a home in the smart home system.

    Attributes:
        name (str): The name of the home.
        description (str): A description of the home.
        image (ImageField): An image representing the home layout.
        is_online (bool): Indicates whether the home is online or not.
        location (str): The location of the home.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='home_layouts')
    is_online = models.BooleanField(default=True)
    location = models.CharField(max_length=255, null=True, blank=True) 
    
    def __str__(self):
        return self.name
    

class Room(TimeStampedModel):
    """
    Represents a room in a home.

    Attributes:
        home (Home): The home to which the room belongs.
        name (str): The name of the room.
        description (str, optional): A description of the room.
        floor (int): The floor number where the room is located.
    """

    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class Light(TimeStampedModel):
    """
    Represents a light device in a room.

    Attributes:
        room (Room): The room to which the light belongs.
        model (str): The model of the light.
        is_online (bool): Indicates whether the light is online or not.

    Methods:
        __str__(): Returns a string representation of the light.

    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices')
    model = models.CharField(max_length=255)
    is_online = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.model} - {self.room}'
    
    
    
class LightningConfigurations(models.Model):
    """
    Model representing the lightning configurations.

    Attributes:
        color (str): The color of the lightning configuration in hexadecimal format.
        brightness (int): The brightness level of the lightning configuration.
        light (Light): The light to which the configuration belongs.
    """
    light = models.OneToOneField(Light, on_delete=models.CASCADE, related_name='configurations', null=True, blank=True)
    color = models.CharField(max_length=7, default='#ffffff')
    brightness = models.IntegerField(default=100)
    theme = models.ForeignKey(LightningScenes, on_delete=models.CASCADE, related_name='configurations', null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f'{self.light.model}-{self.light.room}' if self.light else self.color
    
    @property
    def current_theme(self):
        return self.theme.name if self.theme else 'Custom'
    
    