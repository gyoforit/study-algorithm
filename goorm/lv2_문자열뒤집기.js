// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	let str = ''
	for (let i of line) {
		str = i + str
	}
	console.log(str)
	rl.close();
}).on("close", function() {
	process.exit();
});