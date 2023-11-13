module dump();
	initial begin
		$dumpfile ("timer.vcd");
		$dumpvars (0, tb);
		#1;
	end
endmodule
