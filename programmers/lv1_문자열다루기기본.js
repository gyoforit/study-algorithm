function solution(s) {
  if (s.length !== 4 && s.length != 6) {
      return false
  }
  for (let i of s) {
      let num = Number(i)
      if (!Number.isInteger(num)) {
          return false
      }
  }
  return true
}