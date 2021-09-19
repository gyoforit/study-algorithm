function solution(strings, n) {
  var answer = [];
  var dict = new Object()
  var keys = []
  for (var string of strings) {
      var tmp = string[n]
      if (!dict[tmp]) {
          dict[tmp] = [string]
          keys.push(tmp)
      } else {
          dict[tmp].push(string)
      }
  }
  keys.sort()
  for (var key of keys) {
      var vals = dict[key]
      vals.sort()
      for (var val of vals) {
          answer.push(val)
      }
  }
  return answer;
}