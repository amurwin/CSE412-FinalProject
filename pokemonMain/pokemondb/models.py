from django.db import models

class Move(models.Model):
    name = models.CharField(max_length=27, primary_key=True)
    m_type = models.CharField(max_length=8)
    category = models.CharField(max_length=8, null=True,blank=True)
    power = models.FloatField(null=True,blank=True)
    accuracy = models.FloatField(null=True,blank=True)
    pp = models.FloatField(null=True,blank=True)


class pokeMove(models.Model):
    pokemon = models.ForeignKey("Pokemon", to_field="name", on_delete=models.CASCADE)
    move = models.CharField(max_length=16, null=True,blank=True)


class Ability(models.Model):
    name = models.CharField(max_length=16, primary_key=True)
    description = models.CharField(max_length=137)


class pokeAbility(models.Model):
    name = models.ForeignKey("Pokemon", to_field="name", on_delete=models.CASCADE)
    ability = models.CharField(max_length=16)


class appearance(models.Model):
    types = models.CharField(max_length=23)
    picture = models.CharField(max_length=66)
    unique = models.ForeignKey("Pokemon", to_field="pokedex_no", on_delete=models.CASCADE)
    appearance_id = models.IntegerField(primary_key=True)
    form = models.CharField(max_length=22)


class Pokemon(models.Model):
    unique_id = models.IntegerField()
    pokedex_no = models.IntegerField(unique=True)
    pokedex_entry = models.CharField(max_length=218)
    name = models.CharField(max_length=17, unique=True)
    weight = models.CharField(max_length=21)
    height = models.CharField(max_length=15)
    generation = models.IntegerField()

    class Meta:
        unique_together = (("pokedex_no", "name"))
