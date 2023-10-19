def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i,int):
            return tpl
        result = (srted(tpl))
        return result

def slicer(tpl,element):
    if element not in tpl:
        return()
    if tpl.count(element)== 1:
        return (tpl[tpl.index(element):])
    elif tpl.count(element) == 2:
        s = ''
        for i in tpl:
            s += str(i)
        return tpl[s.index(str(element)):s.rindex(str(element))+1]

def sieve(tpl):
    tpl = tuple(set(tpl))
    return tuple(reversed(tpl))


def del_from_tuple(tpl, element):
    if element not in tpl:
        print('не в кортеже')
        return tpl
    
    s = []
    for i in tpl:
        s.append(i)
    s.remove(element)
    
    return tuple(s)

def good_students(students):
    avg = 0
    for student in students:
        avg += student[2]
    avg /= len(students)


    names = []
    for student in students:
        if student[2] > avg:
            names.append(student[0])

    shortNames = ''
    for name in names:
        end = name.index(' ')
    shortNames += f'{name[:end]},'
    return f"Ученики {shortNames[:-2]} получают хорошие оценки в этом семестре"

students = (('Кожевников Марк Евгеньевич', 17, 4.2, 'Новосибирск'),
            ("Кондратенко Дмитрий Александрович", 17, 3.9, "Чик"),
            ("Сапельников Денис Алексеевич", 16, 3.7, "Новосибирск"),
            ("Федулов Дмитрий Игоревич", 17, 4.5, "Новосибирск"),
            ("Винговатов Александр Олегович", 17, 3.8, "Новосибирск"),
            ("Капустин Кирилл Максимович", 17, 4.1, "Новосибирск"),
            ("Меркулов Владимир Сергеевич", 17, 4.5, "Новосибирск"))
print(good_students(students))
                
