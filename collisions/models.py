from django.db import models

# Create your models here.


class Violations_cameras(models.Model):
    year = models.CharField('Год', max_length=4)
    id_violations = models.CharField('id нарушения', max_length=15, unique=True)
    date = models.CharField('Дата', max_length=10) # "DD/MM/YYYY"
    time = models.CharField('Время', max_length=8) # "HH:MM:SS"
    date_time = models.CharField('Дата, время', max_length=20) # "YYYY-MM-DD HH:MM:SS"
    id_cameras = models.CharField('id камеры', max_length=25)
    model_cameras = models.CharField('Модель камеры', max_length=25)
    type_cameras = models.CharField('Тип камеры', max_length=25)
    # latitude = models.CharField('Широта', max_length=9)
    latitude = models.DecimalField('Широта', max_digits=8, decimal_places=6)  # Виджетом формы по умолчанию для
    # этого поля является NumberInput, когда localize False или TextInput в противном случае.
    # longitude = models.CharField('Долгота', max_length=9)
    longitude = models.DecimalField('Долгота', max_digits=8, decimal_places=6)  # Виджетом формы по умолчанию для
    # этого поля является NumberInput, когда localize False или TextInput в противном случае.
    article_offenses_in_CODE = models.CharField('Статья правонарушения в КОАП', max_length=20)
    content_article = models.CharField('Содержание статьи', max_length=100, blank=True)
    speed_of_violation = models.IntegerField('Зафиксированная скорость в момент нарушения, км/ч')


class Dtp(models.Model):
    year = models.CharField('Год', max_length=4)
    number_accident = models.CharField('Номер', max_length=20)
    date = models.CharField('Дата', max_length=10) # "DD.MM.YYYY"
    time = models.CharField('Время', max_length=8) # "HH:MM:SS"
    type_accident = models.CharField('Вид ДТП', max_length=50)
    place = models.CharField('Место', max_length=100)
    street = models.CharField('Улица', max_length=50, blank=True)
    home = models.CharField('Дом', max_length=20, blank=True)
    road = models.CharField('Дорога', max_length=100, blank=True)
    kilometer = models.CharField('Километр', max_length=10, blank=True)
    metre = models.CharField('Метр', max_length=5, blank=True)
    latitude_degrees = models.CharField('Широта, градусы', max_length=4)
    latitude_minutes = models.CharField('Широта, минуты', max_length=4)
    latitude_seconds = models.CharField('Широта, секунды', max_length=4)
    longitude_degrees = models.CharField('Долгота, градусы', max_length=4)
    longitude_minutes = models.CharField('Долгота, минуты', max_length=4)
    longitude_seconds = models.CharField('Долгота, секунды', max_length=4)
    lost = models.CharField('Погибло', max_length=10, blank=True)
    lost_children = models.CharField('Погибло детей', max_length=10, blank=True)
    wounded = models.CharField('Ранено', max_length=10, blank=True)
    wounded_children = models.CharField('Ранено детей', max_length=10, blank=True)
    division_reg_accident = models.CharField('Подразделение, оформившее ДТП', max_length=100)
    ndu = models.CharField('НДУ', max_length=100)
    ndu_1 = models.CharField('НДУ.1', max_length=100, blank=True)
    ndu_2 = models.CharField('НДУ.2', max_length=100, blank=True)
    ndu_3 = models.CharField('НДУ.3', max_length=100, blank=True)
    uds_objects_in_place = models.CharField('Объекты УДС на месте', max_length=100)
    uds_objects_in_place_1 = models.CharField('Объекты УДС на месте.1', max_length=100, blank=True)
    uds_objects_nearby = models.CharField('Объекты УДС вблизи', max_length=100)
    uds_objects_nearby_1 = models.CharField('Объекты УДС вблизи.1', max_length=100, blank=True)
    uds_objects_nearby_2 = models.CharField('Объекты УДС вблизи.2', max_length=100, blank=True)
    uds_objects_nearby_3 = models.CharField('Объекты УДС вблизи.3', max_length=100, blank=True)
    factors_of_driving_mode = models.CharField('Факторы, влияющие на режим движения', max_length=200)
    factors_of_driving_mode_1 = models.CharField('Факторы, влияющие на режим движения.1', max_length=200, blank=True)
    factors_of_driving_mode_2 = models.CharField('Факторы, влияющие на режим движения.2', max_length=200, blank=True)
    factors_of_driving_mode_3 = models.CharField('Факторы, влияющие на режим движения.3', max_length=200, blank=True)
    condition_of_carriageway = models.CharField('Состояние проезжей части', max_length=100)
    weather_condition = models.CharField('Состояние погоды', max_length=100)
    weather_condition_1 = models.CharField('Состояние погоды.1', max_length=100, blank=True)
    lighting = models.CharField('Освещение', max_length=100)
    concentration_accidents = models.CharField('Является местом концентрации ДТП', max_length=10, blank=True)
    road_on_plan = models.CharField('Дорога в плане', max_length=20)
    profile_of_road = models.CharField('Профиль дороги', max_length=500)
    number_of_lanes = models.CharField('Количество полос', max_length=10, blank=True)
    lane_where_accident = models.CharField('Полоса, в которой произошло ДТП', max_length=10, blank=True)
    width_roadway = models.CharField('Ширина проезжей части', max_length=10, blank=True)
    width_shoulder = models.CharField('Ширина обочины', max_length=10, blank=True)
    width_sidewalk = models.CharField('Ширина тротуара', max_length=10, blank=True)
    width_dividing_strip = models.CharField('Ширина разделительной полосы', max_length=10, blank=True)
    type_dividing_strip = models.CharField('Вид разделительной полосы', max_length=100)
    type = models.CharField('Вид покрытия', max_length=100)
    # latitude = models.CharField('Широта', max_length=9)
    latitude = models.DecimalField('Широта', max_digits=8, decimal_places=6)  # Виджетом формы по умолчанию для
    #  этого поля является NumberInput, когда localize False или TextInput в противном случае.
    # longitude = models.CharField('Долгота', max_length=9)
    longitude = models.DecimalField('Долгота', max_digits=8, decimal_places=6)  # Виджетом формы по умолчанию для
    #  этого поля является NumberInput, когда localize False или TextInput в противном случае.
    location = models.CharField('location', max_length=10, default='other')


class Test(models.Model):
    first_name = models.CharField('Имя', max_length=10)
    last_name = models.CharField('Фамилия', max_length=10)


class PlaceOfCollisions(models.Model):
    """ модель места концентрации ДТП """
    latitude = models.DecimalField('широтка центра места концентрации ДТП', max_digits=8)
    longitude = models.DecimalField('долгота центра места концентрации ДТП', max_digits=8)
    location = models.CharField('расположение город/вне города', max_length=50)

