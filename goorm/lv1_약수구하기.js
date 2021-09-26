// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	let array = new Array()
	for (let i = 1; i <=line; i++) {
		if (line%i === 0) {
			array.push(i)
		}
	}
	console.log(array.join(' ')+' ')
	rl.close();
}).on("close", function() {
	process.exit();
});