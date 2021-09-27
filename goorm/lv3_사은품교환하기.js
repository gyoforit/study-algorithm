// Run by Node.js
const readline = require('readline')

(async () => {
	let rl = readline.createInterface({ input: process.stdin })
	let N = 0
	for await (const line of rl) {
		if (!N) {
			N = +line
		} else {
			let coupons = line.split(' ').map(i => BigInt(i))
			let a = (coupons[0]+coupons[1])/12n
			let b = coupons[0]/5n
			let answer = a > b ? b : a
			console.log(String(answer))
		}
	}
	rl.close()
	
	process.exit()
})()