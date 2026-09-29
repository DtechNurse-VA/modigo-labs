def compare_hobbies(person1_hobbies, person2_hobbies):
    # TODO: use set operations to find shared, only_person1, and only_person2 hobbies
    hobby = {'shared' : (set(person1_hobbies)) & set(person2_hobbies), 'only_person1' : set(person1_hobbies) - set(person2_hobbies), 'only_person2' : set(person2_hobbies) - set(person1_hobbies)}

    return hobby


print(compare_hobbies({"reading", "cording"}, {"cording", "gaming"}))