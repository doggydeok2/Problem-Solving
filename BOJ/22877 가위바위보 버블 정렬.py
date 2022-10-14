can_win = {'R': 'S', 'S': 'P', 'P': 'R'}
cannot_win = {'R': 'P', 'S': 'R', 'P': 'S'}

N, T = map(int, input().split())
cards = list(input())
card_count = {'R': 0, 'S': 0, 'P': 0}
able_to_move_left = [0] * N
for idx, card in enumerate(cards):
    able_to_move_left[idx] = 0 if card_count[can_win[card]] else card_count[cannot_win[card]]
    if card_count[can_win[card]] and card_count[cannot_win[card]]:
        card_count[cannot_win[card]] = 0
    card_count[can_win[card]] = 0
    card_count[card] += 1

ans = [card for card in cards]
for idx, card in enumerate(cards):
    if able_to_move_left[idx] != 0:
        swap_target_idx = idx - min(T, able_to_move_left[idx])
        ans[swap_target_idx], ans[idx] = ans[idx], ans[swap_target_idx]
print(''.join(ans))


# test
# ------------
# import random

# def test():
#     cd = 'SRP'

#     for _ in range(50):
#         cards = [cd[random.randrange(0, 3)] for _ in range(random.randint(1, 50))]
#         check = ''.join(cards)
#         N, T = len(cards), random.randint(1, 1000)

#         card_count = {'R': 0, 'S': 0, 'P': 0}
#         able_to_move_left = [0] * N
#         for idx, card in enumerate(cards):
#             able_to_move_left[idx] = 0 if card_count[can_win[card]] else card_count[cannot_win[card]]
#             if card_count[can_win[card]] and card_count[cannot_win[card]]:
#                 card_count[cannot_win[card]] = 0
#             card_count[can_win[card]] = 0
#             card_count[card] += 1

#         ans = [card for card in cards]
#         for idx, card in enumerate(cards):
#             if able_to_move_left[idx] != 0:
#                 swap_target_idx = idx - min(T, able_to_move_left[idx])
#                 ans[swap_target_idx], ans[idx] = ans[idx], ans[swap_target_idx]

#         for _ in range(T):
#             for i in range(1, N):
#                 if cards[i - 1] == 'R' and cards[i] == 'S' or \
#                         cards[i - 1] == 'S' and cards[i] == 'P' or \
#                         cards[i - 1] == 'P' and cards[i] == 'R':
#                     cards[i - 1], cards[i] = cards[i], cards[i - 1]

#         if ''.join(ans) != ''.join(cards):
#             print('-----')
#             print(len(check), T)
#             print(check)
#             print('yours:' + ''.join(ans))
#             print('__ans:' + ''.join(cards))