def search_relations_for_person(person, relation_table):
    friends = []
    for p1, p2 in relation_table:
        if p1 == person:
            friends.append(p2)
        elif p2 == person:
            friends.append(p1)

    return friends



