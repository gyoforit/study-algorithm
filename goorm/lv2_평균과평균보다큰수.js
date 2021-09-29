// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N
let nums
rl.on("line", function(line) {
	if (!N) {
		N = line
	} else if (!nums) {
		nums = line.split(' ').map(i => +i)
	} else {
		rl.close();
	}
}).on("close", function() {
	const avg = (nums.reduce((acc, ele) => acc+ele, 0)/N).toFixed(1)
	let cnt = 0
	let newNums = nums.filter((ele) => {
		return ele > avg
	})
	console.log(avg, newNums.length)
	process.exit();
});