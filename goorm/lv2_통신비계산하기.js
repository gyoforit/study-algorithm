// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let pay
rl.on("line", function(line) {
	pay = line.split(' ').map(i => +i)
	rl.close();
}).on("close", function() {
	const rateplans = [29900, 34900, 39900, 49900, 59900, 69900]
	const data = [300, 1000, 2000, 6000, 11000, 987654321456456]
	let result = new Array(6)
	let plusRate = 0
	for (let i in rateplans) {
		const now = pay[0]
		const nowData = pay[1]
		// 추가요금
		// console.log(nowData-data[i])
		if (nowData < data[i]) {
			plusRate = 0
		} else if (nowData-data[i] < 5000) {
			if ((nowData-data[i])*20 < 25000) {
				plusRate = (nowData-data[i])*20
			} else {
				plusRate = 25000
			}
		} else {
			plusRate = Math.min((nowData-data[i])*20, 180000)
		}
		// console.log(rateplans[i], plusRate)
		let total = rateplans[i]+plusRate
		result[i] = total
	}
	const recommend = rateplans[result.indexOf(Math.min(...result))]
	console.log(recommend, result[rateplans.indexOf(pay[0])], Math.min(...result))
	process.exit();
});