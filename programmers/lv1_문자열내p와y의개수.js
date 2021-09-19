function solution(str){
  var cntP = 0
  var cntY = 0
  var newStr = str.toLowerCase()
  for (var s of newStr) {
      if (s === 'p') {
          cntP ++
      } else if (s === 'y') {
          cntY ++
      }
  }
  return cntP === cntY ? true : false
}