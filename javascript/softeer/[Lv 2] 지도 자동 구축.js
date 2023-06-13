// https://softeer.ai/practice/info.do?idx=1&eid=413

const N = require('fs').readFileSync('/dev/stdin').toString().trim()
let x = 3
for(let i = 2; i <= N; i++){
    x += x-1
}
console.log(Math.pow(x,2))
