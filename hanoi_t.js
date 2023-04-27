let readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N;
rl.on("line", (line) => {
  N = Number(line);
  console.log(N);
});


const solution = hanoi_t(N, from, tmp, to) {
  const num =(N + "").split(" ").map((s) => +s);
  const [from, tmp, to] = [num[0], num[1], num[2]];
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    console.log(from + "를 " + to + "로 이동");
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
};
process.stdin.on("number", solution);
