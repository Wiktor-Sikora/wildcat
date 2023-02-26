from django.db.models import Min

def m(producttag):
    min_objects = producttag.objects.all().aggregate(min_value=Min('number'))['min_value']
    results = producttag.objects.filter(number=min_objects)[:10]


    for result in results:
        print(result)