people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'age': 24,
        'gender': "female",
        "ex": ["Кирил", "Петър"],
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'age': 34,
        'gender': "female",
        "ex": ["Борис"],
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'age': 18,
        'gender': "female",
        "ex": ['Димитър'],
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'age': 19,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'age': 26,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'age': 34,
        'gender': "male",
        'ex': ['Дарина'],
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'age': 22,
        'gender': "male",
        'ex': ['Галя'],
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'age': 23,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Калоян",
        'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
        'age': 29,
        'gender': "male",
        'ex': [],
    },
]

mathes = []
people_len = len(people)
max_age_range = 6

for idx_person_one, person_one in enumerate(people):
    if person_one['gender'] == 'male':
        search_gender = 'female'
    elif person_one['gender'] == 'female':
        search_gender = 'male'
    else:
        # skip loop cycle when gender is not definite or have anather
        # value from male/female
        continue

    for idx_person_two in range(idx_person_one + 1, people_len):
        person_two = people[idx_person_two]
        compare_persons_age = []
        compare_persons_age.append(person_one['age'])
        compare_persons_age.append(person_two['age'])
        compare_persons_age.sort()

        if person_two['gender'] is not search_gender:
            continue
        if person_one['name'] is person_two['ex']:
            continue
        if compare_persons_age[1] - compare_persons_age[0] > max_age_range:
            continue

        interests_person_one = set(person_one['interests'])
        interests_person_two = set(person_two['interests'])
        interests_common = interests_person_one.intersection(interests_person_two)

        if interests_common:
            mathes.append([person_one['name'], person_one['age'],
                           person_two['name'], person_two['age'],
                           interests_common])

for match in mathes:
    print(match[0] + '(' +str(match[1]) + ')' + " и "
          + match[2] + '(' +str(match[3]) + ') - общ интерес: '
          + ", ".join(match[4]))
