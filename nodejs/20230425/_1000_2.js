const solution = (input) => {
  const [a, b] = (input + "").split(" ").map((s) => +s);
  console.log(a + b);
};
process.stdin.on("data", solution);
