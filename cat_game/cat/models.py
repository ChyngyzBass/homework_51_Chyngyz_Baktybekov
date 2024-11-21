from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(default=1)
    hunger = models.PositiveIntegerField(default=40)
    happiness = models.PositiveIntegerField(default=40)
    is_playing = models.BooleanField(default=False)

    AVATAR_HAPPY = "static/cat_happy.png"
    AVATAR_SAD = "static/cat_sad.png"
    AVATAR_TIRED = "static/cat_tired.png"
    
    @property
    def get_avatar(self):
        """Возвращает путь к изображению в зависимости от уровня счастья кота"""
        if self.happiness > 80:
            return self.AVATAR_HAPPY
        elif self.happiness < 65:
            return self.AVATAR_SAD
        else:
            return self.AVATAR_TIRED

    def feed(self):
        """Увеличить сытость кота"""
        if self.hunger < 100:
            self.hunger += 15
        if self.hunger > 100:
            self.hunger = 10
        if self.happiness < 100:
            self.happiness += 5
        if self.happiness > 100:
            self.happiness = 10
        self.save()

    def play(self):
        """Играть с котом - повышаем уровень счастья"""
        if self.happiness <= 100:
            self.happiness += 15
        if self.happiness > 100:
            self.happiness = 100
        if self.happiness == 100:
            self.happiness -= 40
        if self.hunger < 100:
            self.hunger -= 10
        if self.hunger < 10:
            self.hunger = 10
        self.is_playing = True
        self.save()

    def sleep(self):
        """Успокаиваем кота, снижаем уровень сытости, но повышаем счастье"""
        if self.hunger > 10:
            self.hunger -= 10
        if self.happiness < 100:
            self.happiness += 10
        self.save()

    def __str__(self):
        return self.name or "Неизвестный кот"
