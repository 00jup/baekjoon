const testline = require("readline");

const rl = testline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (TestNN) => {
  console.log("HELLOWWW");
  if (TestNN == "end") rl.close();
});

rl.on("close", () => {
  console.log("END!");
});
