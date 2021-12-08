function solution(numbers, hand) {
  let left = [0, 3],
      right = [2, 3];
  
  return numbers.map(number => {
      switch (number) {
          case 1:
          case 4:
          case 7:
              left = [0, Math.floor(number / 3)];
              return "L";
          case 2:
          case 5:
          case 8:
          case 0:
              let hand_pos = [1, number ? Math.floor(number / 3) : 3];
              let left_dist = Math.abs(hand_pos[0] - left[0]) + Math.abs(hand_pos[1] - left[1]),
                  right_dist = Math.abs(hand_pos[0] - right[0]) + Math.abs(hand_pos[1] - right[1]);
              if (left_dist < right_dist || left_dist === right_dist && hand === "left") {
                  left = [...hand_pos];
                  return "L";
              } else {
                  right = [...hand_pos];
                  return "R";
              }
          case 3:
          case 6:
          case 9:
              right = [2, (number - 3) / 3];
              return "R";
          default:
              break;
  }
  }).join('');
}