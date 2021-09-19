/* filter 함수
array.filter(callback(element[, index[, array]]))
배열의 각 요소에 대해 콜백 함수를 한번씩 실행
콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
*/

function solution(arr, divisor) {
  var answer = arr.filter((num) => {
      if (!(num % divisor)) {
          return true
      }
      return false
  })
  answer.sort(function(f, s) {return f-s})
  if (answer.length > 0) {
      return answer   
  } else {
      return [-1]
  }
}

// 자바스크립트에서 숫자 정렬하는 법
// array.sort((a, b) => a-b) : 오름차순
// array.sort((a, b) => b-a) : 내림차순

// 짧은 버전
function solution(arr, divisor) {
  var answer = arr.filter(v => v%divisor == 0);
  return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}