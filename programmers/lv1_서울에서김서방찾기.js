// js 보간법: `문자열 ${변수} 넣어서 쓰기`
function solution(seoul) {
  for (let i in seoul) {
      if (seoul[i] === 'Kim') {
          return `김서방은 ${i}에 있다`
      }
  }
}

// indexOf 메서드 활용
function solution(seoul) {
  let idx = seoul.indexOf('Kim')
  return `김서방은 ${idx}에 있다`
}