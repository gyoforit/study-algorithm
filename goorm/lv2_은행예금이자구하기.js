// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	let nums = line.split(' ').map(i => +i)
	let first = nums[0]
	for (let i=0; i<nums[2]; i++) {
		first *= (nums[1]*0.01)+1
	}
	console.log(first.toFixed(2))
	rl.close();
}).on("close", function() {
	process.exit();
});