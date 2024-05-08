cook_book={}
with open('files/recipes.txt', encoding='utf-8') as f:
   for line in f:
       #print(line)
       dict_1=[]
       cook_name=line.strip()
       cook_count=f.readline()
       #print(cook_count)
       for i in range(int(cook_count)):
           ingr=f.readline()
           ingr_,quan_,meas_ = ingr.strip().split('|')
           dict_1.append({'ingredient_name':ingr_, 'quantity':quan_,'measure':meas_ })
           part_cook_book={cook_name:dict_1}
       f.readline() #читаем пустую строку
       cook_book.update(part_cook_book)
print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
    cooking_={}
    cook_book1=cook_book
    for dish in dishes:
        if dish in cook_book1:
            for ingr in cook_book1[dish]:
                cooking_.setdefault(ingr['ingredient_name'],)
                if cooking_[ingr['ingredient_name']]==None:
                    cooking_[ingr['ingredient_name']]={'measure':ingr['measure'],'quantity':int(ingr['quantity'])*person_count}
                else:
                    cooking_[ingr['ingredient_name']]['quantity']+=int(ingr['quantity'])*person_count
    return(cooking_)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))