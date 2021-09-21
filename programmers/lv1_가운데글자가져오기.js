function solution(s) {
  const L = s.length
  if (L%2) {
      return s[parseInt(L/2)]
  } else {
      return s[(L/2)-1]+s[L/2]
  }
}

// substr 메서드 사용
function solution(s) {
  const L = s.length
  return L%2 ? s.substr(parseInt(L/2), 1) : s.substr((L/2)-1, 2)
}