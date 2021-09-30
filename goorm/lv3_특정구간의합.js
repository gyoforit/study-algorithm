// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N = null
let nums = null
let idx = null
rl.on("line", function(line) {
	if (!N) {
		N = +line
	} else if (!nums) {
		nums = line.split(' ').map(i => +i)
	} else if (!idx) {
		idx = line.split(' ').map(i => +i)
	} else {
		rl.close();
	}
}).on("close", function() {
	// console.log(N, nums, idx)
	let ans = 0
	for (let i=idx[0]; i<=idx[1]; i++) {
		ans += nums[i-1]	
	}
	console.log(ans)
	process.exit();
});