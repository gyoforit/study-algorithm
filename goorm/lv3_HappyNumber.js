// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N = null
rl.on("line", function(line) {
	N = +line
	rl.close();
}).on("close", function() {
	let now = N
	let tmp = now.toString().split('').map(i => +i)
	let numList = new Set()
	// console.log(tmp)
	while (true) {
		let tmp = now.toString().split('').map(i => +i)
		let result = tmp.reduce((acc, ele) => acc+(ele)**2, 0)
		if (numList.has(result) || result === 1) {
			now = result
			break
		}
		numList.add(result)
		now = result
	}
	let answer = now === 1 ? `${N} is Happy Number.` : `${N} is Unhappy Number.`
	console.log(answer)
	process.exit();
});