// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N = 0
rl.on("line", function(line) {
	N = Number(line)
	rl.close();
}).on("close", function() {
	let answer = 0
	for (let i=1; i<=N; i++) {
		if (i%3 === 0 || i%5 === 0) {
			answer += i
		}
	}
	console.log(answer)
	process.exit();
});