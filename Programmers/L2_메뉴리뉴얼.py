# from collections import Counter
# from itertools import combinations

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = [] # 모든 가능한 조합
#         for order in orders:
#             order_combinations += combinations(sorted(order), course_size)

#         most_ordered = Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]

from itertools import combinations

def solution(orders, course):
    menu = {}

    for i, order in enumerate(orders):
        for o in order:
            try: menu[o].add(i)
            except: menu[o] = {i}

    max_cnt = [0]*len(course)
    li = [[] for _ in range(len(course))]

    for order in orders:
        for i, c in enumerate(course):
            for case in combinations(order, c):
                stack = []
                for a in case:
                    stack.append(menu[a])

                t = stack[0]
                for s in range(1, len(stack)):
                    t = t.intersection(stack[s])

                if len(t) > max_cnt[i]:
                    max_cnt[i] = len(t)
                    li[i] = [''.join(sorted(case))]
                elif len(t) == max_cnt[i]:
                    li[i].append(''.join(sorted(case)))
    answer = []
    for i in range(len(course)):
        if max_cnt[i] >= 2:
            answer += list(set(li[i]))

    return sorted(answer)