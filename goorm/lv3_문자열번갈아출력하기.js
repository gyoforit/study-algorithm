// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let word = ''
rl.on("line", function(line) {
	word = line
	rl.close();
}).on("close", function() {
	let answer = ''
	let s = 0
	let e = word.length-1
	let num = word.length % 2 ? parseInt(word.length/2) : word.length/2
	for (let i=0; i<num; i++) {
		answer += word[s]
		s ++
		answer += word[e]
		e --
	}
	if (word.length%2) {
		answer += word[num]
	}
	console.log(answer)
	process.exit();
});