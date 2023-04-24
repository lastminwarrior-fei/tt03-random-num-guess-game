`default_nettype none
`timescale 1ns/1ps

module tb (
    input wire clk,
    input wire rst,
    input wire [5:0] guess,
    output wire [5:0] result    
    );

    initial begin
        $dumpfile ("tb.vcd");
        $dumpvars (0, tb);
        #1;
    end

    wire [7:0] inputs = {guess[5:0], rst, clk};
    wire [7:0] outputs;
    assign result = outputs[5:0]; 

    guess_game guess_game (
        .io_in (inputs),
        .io_out (outputs)
    );

endmodule
