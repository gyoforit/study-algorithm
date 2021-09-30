// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N = null
let cntN = 0
let word = []
rl.on("line", function(line) {
	if (!N) {
		N = +line
	} else {
		word.push(line.split(' '))
		cntN ++
	}
	if (cntN === N) {
		rl.close();
	}
}).on("close", function() {
	let answer = ''
	for (let j=N-1; j>=0; j--) {
		for (let i=0; i<N; i++) {
			answer += word[i][j]
		}
	}
	console.log(answer)
	process.exit();
});