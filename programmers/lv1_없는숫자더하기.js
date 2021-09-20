/*
reduce method
array.reduce((acc, element, idx, array) => {'do something'}, initialValue)
callback 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
acc: 이전 callback함수의 반환 값이 누적되는 변수
initialValue: 최초 callback 함수 호출 시 acc에 할당하는 값. 제공하지 않으면 배열의 첫번째값 사용
*/

function solution(numbers) {
  var reducer = (accumulator, curr) => accumulator + curr
  var before = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  var total = before.reduce(reducer)
  return total - numbers.reduce(reducer)
}

// 간편 버전
function solution(numbers) {
  return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}