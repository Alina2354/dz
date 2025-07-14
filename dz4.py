def find_uniq_interes(users):
    all_interests = set()
    for interests in users.values():
        all_interests.update(interests)
    return all_interests

def find_common_interes(users):
    common_interest_pairs = []
    for user1, interests1 in users.items():
        for user2, interests2 in users.items():
            if user1 != user2 and (user1, user2) not in common_interest_pairs and (user2,user1) not in common_interest_pairs:
                if interests1.intersection(interests2):
                    common_interest_pairs.append((user1, user2))
    return common_interest_pairs


def max_common_iteres(users, common_interest_pairs):
    max_common_interests = 0
    best_pair = None
    best_common_interests_set = None
    for user1, user2 in common_interest_pairs:
        interests1 = users[user1]
        interests2 = users[user2]
        common_interests = interests1.intersection(interests2)
        num_common_interests = len(common_interests)

        if num_common_interests > max_common_interests:
            max_common_interests = num_common_interests
            best_pair = (user1, user2)
            best_common_interests_set = common_interests

    print("3. Пара с наибольшим количеством общих интересов:", best_pair, "(общие интересы:", best_common_interests_set, ")")


if __name__ == '__main__':
    users = {
        "Алексей": {"программирование", "музыка", "кино"},
        "Мария": {"кино", "путешествия", "фотография"},
        "Иван": {"программирование", "спорт", "музыка"},
        "Ольга": {"путешествия", "кино", "фотография"}
    }

    unique_interests = find_uniq_interes(users)
    print(unique_interests)
    common_interest_pairs_result = find_common_interes(users)
    print(common_interest_pairs_result)
    print(max_common_iteres(users, common_interest_pairs_result))