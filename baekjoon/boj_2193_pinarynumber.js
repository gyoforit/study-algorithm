const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim()
input = +input

let pinaryNum = new Array(input+1).fill(0)
pinaryNum[1] = 1
pinaryNum[2] = 1
for (let i=3; i<=input; i++) {
  pinaryNum[i] = BigInt(pinaryNum[i-2])+BigInt(pinaryNum[i-1])
}

console.log(BigInt(pinaryNum[input]).toString())