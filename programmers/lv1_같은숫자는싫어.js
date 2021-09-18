// for...of: iterable한 자료의 원소를 하나씩 순회
function solution(arr)
{
    var answer = []
    var now = -1
    for (let num of arr) {
        if (now != num) {
            answer.push(num)
            now = num
        }
    }
    return answer;
}

console.log(solution([1,1,3,3,0,1,1]))