// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let size
let grid = []
let answer = []
let drc = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
rl.on("line", function(line) {
	if (!size) {
		size = line.split(' ').map(i => +i)
	} else {
		grid.push(line.split(''))
	}
	if (grid.length === size[0]) {
		rl.close();
	}
}).on("close", function() {
	const M = size[0]
	const N = size[1]
  // 정답이 될 배열 초기화
	for (let i=0; i<M; i++) {
		answer.push(new Array(N).fill(0))
	}
  // 지뢰 표시
	for (let r=0; r<M; r++) {
		for (let c=0; c<N; c++) {
			if (grid[r][c] === '*') {
				answer[r][c] = '*'
			}
		}
	}

	for (let r=0; r<M; r++) {
		for (let c=0; c<N; c++) {
			if (grid[r][c] === '*') {
				for (let delta of drc) {
					const nr = r+delta[0]
					const nc = c+delta[1]
          // 인덱스가 범위 내이고, 지뢰가 아닐 때만 +1
					if (0<=nr && nr<M && 0<=nc && nc<N && answer[nr][nc] != '*') {
						answer[nr][nc] += 1
					}
				}
			}
		}
	}
	
	for (let ans of answer) {
		ans = ans.map(i => i.toString())
		console.log(ans.join(''))
	}
	
	process.exit();
});