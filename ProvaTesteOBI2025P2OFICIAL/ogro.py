def result(left_hand, right_hand):
  return (left_hand+right_hand) if left_hand > right_hand else 2 * (right_hand-left_hand)

left = int(input())
right = int(input())

print(result(left, right))