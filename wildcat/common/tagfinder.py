from collections import Counter

def find(product, a):
    products = a.objects.all()
    tags_name = product.tags.all()
    tags_list=[]
    corect_product = []
    for tag in tags_name:
         tags_list.append(tag.name)
         
    for tag in tags_list:
         for item in products:
              item_tags = item.tags.all()
              for i in item_tags:
                   if i.name==tag:
                        corect_product.append(item)

    
    end = Counter(corect_product)
    war = max(end.values())
    naj = max(end, key=end.get)
    print(war, naj.tags.all())

    



    