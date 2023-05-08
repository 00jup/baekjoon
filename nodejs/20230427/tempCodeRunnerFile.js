function hanoi_t(N, A, B, C) {
  if (N === 1) {
    console.log(A, "-->", C);
    return;
  } else {
    hanoi_t(N - 1, A, C, B);
    console.log(A, "-->", C);
    hanoi_t(N - 1, B, A, C);
  }
}
hanoi_t(N, "A", "B", "C");
