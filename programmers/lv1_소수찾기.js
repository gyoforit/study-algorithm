// 에라토스테네스의 체
function solution(n) {
    let nums = []
    for (let i=0; i<=n; i++) {
        nums.push(true)
    }
    for (let i=2; i*i<=n; i++) {
        if (nums[i]) {
            for (let j=i*i; j<=n; j+=i) {
                nums[j] = false
            }
        }
    }
    nums.splice(0, 2, false, false)
    const answer = nums.filter((val) => {
        return val === true
    })
    return answer.length
}