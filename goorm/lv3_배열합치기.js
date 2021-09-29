// Run by Node.js
// 배열 합치는 방법 2가지
// 1. concat 사용
// A = [1, 2, 3] B= [4, 5, 6]
// let C = A.concat(...B) -> [1, 2, 3, 4, 5, 6]
// 2. Spread operator 사용
// let C = [...A, ...B] -> [1, 2, 3, 4, 5, 6]

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N
let arrayA
let arrayB
rl.on("line", function(line) {
	if (!N) {
		N = line.split(' ').map(i => +i)
	} else if (!arrayA) {
		arrayA = line.split(' ').map(i => +i)
	} else if (!arrayB) {
		arrayB = line.split(' ').map(i => +i)
	} else {
		rl.close();
	}
}).on("close", function() {
	let result = [...arrayA, ...arrayB]
	console.log((result.sort((a, b) => a-b)).join(' ') + ' ')
	process.exit();
});