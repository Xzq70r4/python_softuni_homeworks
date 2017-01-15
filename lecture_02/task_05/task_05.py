ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

ivan_interest_set = set(ivan)
maria_interest_set = set(maria)
common_interests = ivan_interest_set.intersection(maria)
print(common_interests)