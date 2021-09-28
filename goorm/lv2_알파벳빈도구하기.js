// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let sentence = ''
rl.on("line", function(line) {
	sentence = line
	rl.close();
}).on("close", function() {
	sentence = sentence.toLowerCase()
	let alphabets = 'abcdefghijklmnopqrstuvwxyz'.split('')
	const L = alphabets.length
	let answer = new Array(L).fill(0)
	for (let i of sentence) {
		if (i != '') {
			answer[alphabets.indexOf(i)] += 1
		}
	}
	
	for (let j=0; j<L; j++) {
		console.log(alphabets[j] + ' : ' + answer[j])
	}
	process.exit();
});