from django.db import models


class Room(models.Model):
    description = models.CharField('Описание номера', max_length=255)
    price = models.IntegerField('Цена номера за ночь', db_index=True)
    date_add = models.DateField('Дата добавления', auto_now=True, db_index=True)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_id')
    date_start = models.DateField(db_index=True)
    date_end = models.DateField()
