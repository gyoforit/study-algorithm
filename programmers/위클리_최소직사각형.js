function solution(sizes) {
  let big = 0
  let small = 0
  sizes.forEach((element) => {
      let mx = Math.max(...element)
      big = Math.max(big, mx)
      let mn = Math.min(...element)
      small = Math.max(small, mn)
  })
  return big*small
}