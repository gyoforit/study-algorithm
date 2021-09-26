// Run by Node.js
/*
goorm 입력 방식
r.close() 가 나오기 전까지는 계속 input을 받는 것!
*/
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let sentence = ''
let word = ''
rl.on("line", function(line) {
	if (!sentence) {
		sentence = line
	} else if (!word) {
		word = line
	} else {
		rl.close();
	}
}).on("close", function() {
	let answer = 0
	for (let w of sentence) {
		if (w === word) answer ++
	}
	console.log(answer)
	process.exit();
});