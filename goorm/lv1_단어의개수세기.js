// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	const arr = line.split(' ')
	let answer = 0
	for (let word of arr) {
		if (word) answer ++
	}
	console.log(answer)
	rl.close();
}).on("close", function() {
	process.exit();
});