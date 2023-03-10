// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

// Example clock gating module for yosys synthesis

module prim_clock_gating (
  input  wire clk_i,
  input  wire en_i,
  input  wire test_en_i,
  output wire clk_o
);

     
`ifdef SYNTHESIS
  `ifndef FPGA  
  //TODO: needs to use 36 since it is the always library that is present! even for run minimal
  //TODO: what defines select the target?

    // You put the smallest drive strength (X1) and then the tool changes it according to the need 
    // SC8T_CKGPRELATNX1_DDC28UH i_SC8T_CKGPRELATNX1_DDC28UH (.CLK(CLKIN), .E(ENABLE), .TE(SE), .Z(CLKOUT));
    
    SC7P5T_CKGPRELATNX1_CSC20L i_SC7P5T_CKGPRELATNX1_CSC20L (.CLK(clk_i), .E(en_i), .TE(test_en_i), .Z(clk_o));
  `else
    `define PRIMITIVE
    
    `ifndef PRIMITIVE
      reg  clk_en;
      wire cfg_acg    = (CBAW == 0) ? (ACG != 0) : 1'b0;

      wire clk_en_nxt = ENABLE | ~cfg_acg;
      wire gated_clk  = CLKIN & clk_en;
      wire clk_out    = cfg_acg ? gated_clk : CLKIN;

      always @(CLKIN or clk_en_nxt)
        if(~CLKIN)
          clk_en <= clk_en_nxt;

      assign CLKOUT   = clk_out;
    `else 
      BUFGCE #(
      .CE_TYPE("SYNC"),               // ASYNC, HARDSYNC, SYNC
      .IS_CE_INVERTED(1'b0),          // Programmable inversion on CE
      .IS_I_INVERTED(1'b0),           // Programmable inversion on I
      .SIM_DEVICE("ULTRASCALE_PLUS")  // ULTRASCALE, ULTRASCALE_PLUS
      )
      BUFGCE_inst (
        .O(CLKOUT),   // 1-bit output: Buffer
        .CE(ENABLE), // 1-bit input: Buffer enable
        .I(CLKIN)    // 1-bit input: Buffer
      );
    `endif
  `endif

`else   
  reg en_latch;

  always @* begin
    if (!clk_i) begin
      en_latch = en_i | test_en_i;
    end
  end

  assign clk_o = en_latch & clk_i;
`endif 

endmodule
