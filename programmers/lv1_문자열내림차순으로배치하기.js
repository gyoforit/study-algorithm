/*
<join>
sample = ['a', 'b', 'c'] -> 'abc'로 만들기 위해서는
파이썬: ''.join(sample)
자바스크립트: sample.join('')
*/
function solution(s) {
  let answer = []
  for (let i of s) {
      answer.push(i)
  }
  answer = answer.sort().reverse().join('')
  return answer
}