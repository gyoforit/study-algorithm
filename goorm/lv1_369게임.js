// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	let answer = 0
	for (let i=1; i<=line-1; i++) {
		const tmp = i.toString()
		for (let j of tmp) {
			if (j === '3' || j === '6' || j === '9') answer ++
		}
	}
	console.log(answer)
	rl.close();
}).on("close", function() {
	process.exit();
});