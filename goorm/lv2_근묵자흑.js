// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let NK
let nums
rl.on("line", function(line) {
	if (!NK) {
		NK = line.split(' ').map(i => Number(i))
	} else if (!nums) {
		nums = line.split(' ').map(i => Number(i))
 	} else {
		rl.close()
	}
}).on("close", function() {
	const minvalIdx = nums.indexOf(Math.min(...nums))
	let answer = 987654321
	for (let i=0; i<NK[1];i++) {
		const front = nums.slice(0, minvalIdx-i)
		const back = nums.slice(minvalIdx+NK[1]-i,nums.length)
		let a = 0
		let b = 0
		let c = NK[1]-1
		if (front.length) {
			a = front.length % c ? parseInt(front.length/c)+1 : parseInt(front.length/c)
		}
		if (back.length) {
			b = back.length % c ? parseInt(back.length/c)+1 : parseInt(back.length/c)
		}
		if (a+b+1 < answer) answer = a+b+1
	}
	console.log(answer)
	process.exit();
});