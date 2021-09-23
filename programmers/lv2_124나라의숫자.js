function solution(n) {
  let answer = ''
  while (n) {
      let tmp = ['4', '1', '2'][n%3]
      answer = tmp + answer
      n = n % 3? parseInt(n/3) : n/3 -1
  }
  return answer;
}