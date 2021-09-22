function solution(n) {
  const m = n%2 ? (n+1)/2 : n/2
  let answer = '수박'.repeat(m)
  answer = (n === 2*m) ? answer : answer.substr(0, n)
  return answer
}