function solution(s) {
  var answer = []
  let words = s.split(' ')
  for (let word of words) {
      let change = ''
      for (let i in word) {
          let tmp = i%2 ? word[i].toLowerCase() : word[i].toUpperCase()
          change += tmp
      }
      answer.push(change)
  }
  return answer.join(' ')
}