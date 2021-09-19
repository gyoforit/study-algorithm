/*
js에서의 최대, 최소, 절댓값은 앞에 Math 붙이기
ex. Math.max(a, b) / Math.min(a, b) / Math.abs(a-b)
*/

function solution(a, b) {
  var answer = 0
  if (a === b) {
      return a
  }
  var big = Math.max(a, b)
  var small = Math.min(a, b)
  for (var i = small; i<=big; i++) {
      answer += i
  }
  return answer;
}