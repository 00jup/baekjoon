let readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function hanoi_t(N, from, tmp, to) {
  if (N >= 1) {
    hanoi_t(N - 1, from, to, tmp);
    console.log(from + "를 " + to + "로 이동");
    hanoi_t(N - 1, tmp, from, to);
  }
  return;
}

hanoi_t(3, "A", "B", "C");

let N = Number(rl.on);
rl.on("line", function (line) {
  N = Number(line);
  hanoi_t(N, "A", "B", "C");
  if (N === 0) rl.close();
});
rl.on("close", function () {
  process.exit();
});
