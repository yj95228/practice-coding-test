function solution(lottos, win_nums) {
    let zeroCount = lottos.filter(x => 0 === x).length;
    let sameCount = lottos.filter(x => win_nums.includes(x)).length;
    let answer = [7-zeroCount-sameCount, 7-sameCount].map(function(num){
        if (num > 6) {num = 6; return num;}
        else {return num;};
    });
    return answer;
}
