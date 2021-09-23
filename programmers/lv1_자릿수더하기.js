function solution(n)
{
    var answer = 0;
    for (let i of n.toString()) {
        let tmp = Number(i)
        answer += tmp
    }

    return answer
}