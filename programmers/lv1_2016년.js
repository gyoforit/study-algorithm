function solution(a, b) {
  const days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
  const months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  let today = months.slice(0, a)
  return days[(today.reduce((acc, element) => acc+element, 0)+b-1)%7]
}