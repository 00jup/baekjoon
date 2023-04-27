let fs = require("fs");
let rl = fs.readFileSync("input.txt").toString().split(" ");

function hanoi_t(N, from, tmp, to) {
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    console.log(from + " " + to);
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
}
function cnt(N) {
  if (N == 1) console.log(1);
  else console.log(2 ** N - 1);
}

let N;
let h_cnt = 0;
N = Number(rl);
cnt(N);
hanoi_t(N, "1", "2", "3");
