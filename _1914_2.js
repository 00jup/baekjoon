let fs = require("fs");
let rl = fs.readFileSync("/dev/stdin").toString().split(" ");

function hanoi_t(N, from, tmp, to) {
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    answer.push([from, to]);
    cnt++;
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
}

let cnt = 0;
let N = Number(rl);
let answer = [];

hanoi_t(N, "1", "2", "3");
console.log(cnt);
console.log(answer.map((element) => element.join(" ")).join("\n"));
