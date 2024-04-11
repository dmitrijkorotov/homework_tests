from typing import List


def unique_names(list_name: List[list]) -> str:
    """
    Returns a unique name from a list of names.
    """
    all_list = []
    for m in list_name:
        all_list += m
         
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])
        

    unique_names = list(set(all_names_list))


    all_names_sorted = sorted(unique_names)
    all_names_sorted = ', '.join(all_names_sorted)

    return f'Уникальные имена преподавателей: {all_names_sorted}'

def popular_names(list_names: List[list]) -> str:
    """
    Returns the most popular name from a list of names.
    """
	
    all_list = []
    for m in list_names:
        all_list += m 

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])
	
    unique_names = list(set(all_names_list))

    all_names_sorted = sorted(unique_names)
    all_names_sorted = ', '.join(all_names_sorted)

    popular = []
    for name in all_names_list:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x:x[1], reverse=True)

    popular_2 = []
    for name in popular:
        if name not in popular_2:
            popular_2.append(name)
		
    top_3 = popular_2[:3]

    result = ''
    for top, quantity in top_3:
        if len(result) > 0:
            result += ', '
        result += f"{top}: {quantity} раз(а)"

    return result

def supernames(courses: List, mentors: List[list]) -> str:
    lists_names = [] 
    for mentor in mentors:
        names = []
        lists_names.append(names)
        for ment in mentor:
            name = ment.split()
            names.append(name[0])
    
    result = ''
    pairs = []
    for l1 in range(len(lists_names)):
        for l2 in range(len(lists_names)):
            if l1 == l2:
                continue
            intersection_names = set(lists_names[l1]) & set(lists_names[l2])
            if len(intersection_names) > 0:
                pair = {courses[l1], courses[l2]}
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(list(intersection_names))
                    result += (f"На курсах '{courses[l1]}' и '{courses[l2]}'"
                    f"преподают: {', '.join(all_names_sorted)}\n")
    return result

if __name__ == "__main__":
    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
    list_names = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    print(unique_names(list_names))
    print(popular_names(list_names))
    print(supernames(courses, list_names))