// https://softeer.ai/practice/info.do?idx=1&eid=409

const [n, ...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s/);
const graph = arr.map(x => x.split('').map(Number))

const dfs = (x, y) => {
    if(x <= -1 || x >= n || y <= -1 || y >= n) return false
    if(graph[x][y] === 1){
        cnt++
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return true
    }
    return false
}

let cnt = 0
let result = 0
const result_list = []
for(let i = 0; i < n; i++){
    for(let j = 0; j < n; j++){
        if(dfs(i, j)){
            result++
            result_list.push(cnt)
            cnt = 0
        }
    }
}
console.log(result)
console.log(result_list.sort((a,b) => a-b).join('\n'))
