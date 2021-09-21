function solution(s) {
  if (s.includes('+') || s.includes('-')) {
      return s.includes('+') ? Number(s.substr(1)) : Number(s.substr(1))*(-1)
  } else {
      return Number(s)
  }  
}