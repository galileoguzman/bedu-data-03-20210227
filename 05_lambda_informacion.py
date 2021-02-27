informacion = {
    'students': [
        {
            'name': 'Galileo Guzman',
            'age': 31,
            'hobbies': ['music', 'movies', 'biking', 'read', 'books']
        },
        {
            'name': 'Omar Flores',
            'age': 18,
            'hobbies': ['troba', 'movies', 'biking', 'read', 'books']
        },
        {
            'name': 'Armando',
            'age': 18,
            'hobbies': ['music', 'read', 'books']
        },
        {
            'name': 'Eduardo',
            'age': 18,
            'hobbies': ['music', 'read', 'books']
        },
    ],
    'last_update': '2021-02-27',
    'modified_by': 'frasgado@mail.io'
}

students_with_hobbies = list(map(hobbies_counter, informacion['students']))
