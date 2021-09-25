const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(/\s/).map(i => parseInt(i))
input.toString().trim().split(/\s/).map(i => parseInt(i))
// console.log(input)
const n = input[0]
const a = input.slice(1, n+1)
const b = input[n+1]
const c = input[n+2]
let count = 0
for (let i of a) {
  count ++
  i -= b
  if (i > 0) {
    let tmp = i%c === 0 ? parseInt(i/c) : parseInt(i/c)+1
    count += tmp
  }
}
console.log(count)