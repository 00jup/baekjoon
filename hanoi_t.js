let readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let N;
rl.on("line", function (line) {
  N = Number(line);
});
rl.close();

function hanoi_t(N, from, tmp, to) {
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    console.log(from + "를 " + to + "로 이동");
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
}
hanoi_t(N, "A", "B", "C");
