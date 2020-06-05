Module c17 (N1, N2, N3, N6, N7, N22, N23);

Input N1, N2, N3, N6, N7;
Output N22, N23;
Wire N10, N11, N16, N19;

Nand NAND2_1 (N10, N1, N3);
Nand NAND2_2 (N11, N3, N6);
Nand NAND2_3 (N16, N2, N11);
Nand NAND2_4 (N19, N11, N7);
Nand NAND2_5 (N22, N10, N16);
Nand NAND2_6 (N23, N16, N19);

Endmodule