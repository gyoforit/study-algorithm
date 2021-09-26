// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	// console.log(line);
	const scores = line.split(' ').map(i => Number(i))
	const avg = (scores.reduce((acc, el) => acc+el)/3).toFixed(2)
	let grade = ''
	if (avg >= 90) {
		grade = 'A'
	} else if (avg >= 80) {
		grade = 'B'
	} else if (avg >= 70) {
		grade = 'C'
	} else if (avg >= 60) {
		grade = 'D'
	} else {
		grade = 'F'
	}
	console.log([avg, grade].join(' '))
	rl.close();
}).on("close", function() {
	process.exit();
});