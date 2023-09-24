let readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function hanoi_t(N, from, tmp, to) {
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    console.log(from + " " + to);
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
}
function cnt(N) {
  if (N == 1) return 1;
  else return 2 ** N - 1;
}

let N;
let h_cnt = 0;
rl.on("line", function (line) {
  N = Number(line);
  h_cnt = cnt(N);
  console.log(h_cnt);
  hanoi_t(N, "1", "2", "3");
  rl.close();
});
