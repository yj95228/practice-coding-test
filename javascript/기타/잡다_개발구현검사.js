function solution(C) {
  // 1단계 function(H,C)
  // let current = H.length-1
  // const answer = C.reduce((a, b) => {
  //     if (b === 'BACK' && a-1 >= 0) a--
  //     if (b === 'NEXT' && a+1 < H.length) a++
  //     return a
  // }, current)
  // return H[answer]

  // 2단계
  const answer = C.reduce(
    (a, b) => {
      console.log(a);
      if (b[0] === "PUSH") return [a[0] + 1, ...a.slice(1, a[0] + 1), b[1]];
      if (b[0] === "BACK") {
        if (Number(b[1]) < a[0]) {
          return [a[0] - Number(b[1]), ...a.slice(1)];
        } else {
          return [1, ...a.slice(1)];
        }
      }
      if (b[0] === "NEXT") {
        if (Number(b[1]) <= H.length - a[0]) {
          return [a[0] + Number(b[1]), ...a.slice(1)];
        } else {
          return [a.length, ...a.slice(1)];
        }
      }
    },
    [0]
  );
  // return answer[answer[0]] // 현재 페이지 반환

  // 3단계
  return [...new Set(answer.slice(1))];
}
