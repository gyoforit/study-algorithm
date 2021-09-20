function division(num) {
  var cnt = 0
  for (var i=1; i<=num; i++) {
      if (!(num%i)) {
          cnt += 1
      }
  }
  return cnt
}

function solution(left, right) {
  var answer = 0
  for (var i=left; i<=right; i++) {
      var tmp = division(i)
      var result = tmp % 2 ? -i : i
      answer += result
  }
  return answer;
}