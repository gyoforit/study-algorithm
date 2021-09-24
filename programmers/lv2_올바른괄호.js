function solution(s){
  let answer = true
  let stack = []
  for (let i of s) {
      if (i === '(') {
          stack.push(i)
      } else if (stack.length && i === ')') {
          stack.pop()
      }
  }
  if (stack.length > 0 || s[0] === ')') answer = false
  return answer
}