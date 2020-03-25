def get_nested_scores(how_many_scores, name_scores_list):
    db = []
    [db.append([x[0], x[1]]) for x in name_scores_list]
    return db


def sorted_by_score_ascending(how_many_scores, name_scores_list):
    db = []
    [db.append([x[0], x[1]]) for x in name_scores_list]
    db = sorted(db, key=lambda x: x[1], reverse=False)
    # or
    # from operator import itemgetter ->>> operator lib
    # (...)
    # db = sorted(db, key=itemgetter(1), reverse=False) # for descending - >> reverse = True
    return db

def find_second_lowest_ordered_by_name(given_scores_list):

    db = sorted_by_score_ascending(len(given_scores_list), given_scores_list)
    new_db = []
    [new_db.append(item) for item in db if item[1] == db[1][1]]

    new_db = sorted(new_db, key=lambda x: x[0], reverse=False)

    if len(new_db) == 1:
        return new_db[0]
    else:
        return new_db

