// Run by Node.js
const solution = (N,K,data) => {
	console.log(data.reduce((a,x) => a += x.includes(K) ? 0 : 1, 0))
}
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = null;
	let K = null;
	const data = [];
	for await (const line of rl) {
		if(!N){
			[N,K] = line.split(' ');
		}else{
			data.push(...line.split(' '));
			rl.close();
		}
	}
	solution(N,K,data);
	process.exit();
})();
