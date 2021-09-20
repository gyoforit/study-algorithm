/*
Set을 쓸 때는 항상 앞에 new 붙이기
처음엔 nums를 new Set()으로 초기화하고 add를 했는데 안 됨. 왜인지는 모르겠음 ㅠ
Set -> Array 변환할 땐 [...set변수명] 을 써서 펼치기
*/

function solution(numbers) {
  var nums = []
  for (let i=0; i<numbers.length-1; i++) {
      for (let j=i+1; j<numbers.length; j++) {
          var tmp = numbers[i]+numbers[j]
          nums.push(tmp)
      }
  }
  return [...new Set(nums)].sort((f, e) => f-e)
}