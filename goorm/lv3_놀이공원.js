// Run by Node.js
const readline = require('readline');

function solution (N, K, grid) {
	let ans = 987654321
	for (let r=0;r<N-K+1;r++) {
		for (let c=0;c<N-K+1;c++) {
			let tmp = 0
			for (let i=0;i<K;i++) {
				for (let j=0;j<K;j++) {
					if (grid[r+i][c+j]) {
						tmp ++
					}
				}
			}
			ans = Math.min(ans, tmp)
		}
	}
	return ans
}
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let T = null
	let num = null
	let ground = []
	let cntN = 0
	let cntT = 0
	for await (const line of rl) {
		if (!T) {
			T = +line
		} else if (!num) {
			num = line.split(' ').map(i => +i)
		} else {
			ground.push(line.split(' ').map(i=>+i))
			cntN ++
		}
		if (num && cntN === num[0]) {
			let answer = solution(num[0], num[1], ground)
			console.log(answer)
      // 한 케이스 종료 후 T를 뺀 나머지 변수들 초기화 후 cntT ++
			num = null
			cntN = 0
			ground = []
			cntT ++
		}
    // T개의 케이스 다 끝내면 종료
		if (cntT === T) {
			rl.close();
		}
	}
	
	process.exit();
})();
