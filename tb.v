`default_nettype none
`timescale 1ns/1ns

/*
this testbench just instantiates the module and makes some convenient wires
that can be driven / tested by the cocotb test.py
*/

module tb (
    // testbench is controlled by test/test_*.py files
	input wire clk_tb,
	input wire enable_tb,
	input wire set_tb,
	input wire direction_tb,
	input wire auto_reload_tb,
	input wire done_ack_tb,
	input wire [15:0] count_tb,
	output wire done_tb
);

    // instantiate the DUT
    timer timer(
        .clk (clk_tb),
        .enable (enable_tb),
        .set (set_tb),
        .direction (direction_tb),
        .auto_reload (auto_reload_tb),
        .done_ack (done_ack_tb),
        .count (count_tb),
        .done (done_tb)
    );

endmodule
