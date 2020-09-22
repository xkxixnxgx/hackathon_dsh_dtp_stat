""" в данном разделе определены инструменты для выявления мест концентрации ДТП """
from geopy import distance
from .models import Dtp, PlaceOfCollisions


def distance_between_collisions(point_1, point_2):
    """ определяет расстояние между двумя авариями """
    # определяем координаты точек
    first_collision = tuple(point_1.latitude, point_1.longitude)
    second_collision = tuple(point_2.latitude, point_2.longitude)
    # определяем расстояние между точками в метрах
    return distance.distance(first_collision, second_collision).km / 1000

def place_of_collisions_outside(year):
    # делаем выборку аварий по фильтрам вне города по соответствующему году
    collisions_outside_data = Dtp.objects.filter(location='outside', year=year)
    for current_collision in collisions_outside_data:
        # если данная точка не входит в место концентрации ДТП делаем проверку
        if current_collision.place_of_collisions is None:
            count = 0  # счетчик аварий на данном участке
            current_collisions_list = []  # список аварий на данном учаске
            # определяем расстояние между соседними авариями
            for collision in collisions_outside_data:
                distance = distance_between_collisions(
                    current_collision,
                    collision
                )
                if distance <= 500:
                    count += 1
                    current_collisions_list.append(collision)

            #  делаем вывод о данной дочке
            if count >= 5:
                new_place_of_collision = PlaceOfCollisions.objects.create(
                    latitude=current_collision.latitude,
                    longitude=current_collision.longitude,
                    location=current_collision.location,
                )
                # присваиваем всем точка, входящим в список аварий принадлежность к новому
                # месту концентрации ДТП
                for collision in current_collisions_list:
                    collision.place_of_collisions = new_place_of_collision
                    collision.save(update_fields=['place_of_collisions'])
