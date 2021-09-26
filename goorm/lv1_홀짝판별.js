// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	const answer = line % 2 ? 'odd' : 'even'
	console.log(answer)
	rl.close();
}).on("close", function() {
	process.exit();
});