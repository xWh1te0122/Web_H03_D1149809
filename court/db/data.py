from court.models import Court

Court.objects.all()

Court1 = Court(courtName='Centre Court', courtType='Grass Court',locationCity = 'London')
Court2 = Court(courtName='Rod Laver Arena', courtType='Hard Court',locationCity = 'Melbourne')
Court3 = Court(courtName='Stade Roland-Garros', courtType='Clay Court',locationCity = 'France')
Court4 = Court(courtName='Arthur Ashe Stadium', courtType='Hard Court',locationCity = 'NewYork')
Courts_list = [Court1, Court2, Court3, Court4]
for x in Courts_list:
    x.save()

Court.objects.all().values()