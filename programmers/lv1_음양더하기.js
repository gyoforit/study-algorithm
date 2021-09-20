function solution(absolutes, signs) {
  var answer = 0
  var L = absolutes.length
  for (var i=0; i<L; i++) {
      var tmp = signs[i] ? absolutes[i] : -absolutes[i]
      answer += tmp
  }
  return answer
}

// reduce 메서드 활용
function solution(absolutes, signs) {
  return absolutes.reduce((acc, val, i) => acc+(val*(signs[i]?1:-1)), 0)
}