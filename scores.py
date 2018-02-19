school_journal = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '5a', 'scores': [5,5,4,3,5,3]},
{'school_class': '6a', 'scores': [3,3,3,3]},
{'school_class': '5b', 'scores': [5,2,2,5,5,4,4]},
{'school_class': '6b', 'scores': [5,4,2,2,4]},
]

#print(school_journal)

#for school_cl, score in school_journal[school_cl]['scores'][score]:
#    pass

all_scores = []

for school_cl in school_journal:
    cl_scores = school_cl['scores']
    cl_name = school_cl['school_class']
    average_cl_score = round(sum(cl_scores) / len(cl_scores))
    print('Средняя оценка в классе {} - {}'.format(cl_name, average_cl_score))

    all_scores += cl_scores

average_all_score = round(sum(all_scores) / len(all_scores))
print('Средняя оценка в школе - {}'.format(average_all_score))