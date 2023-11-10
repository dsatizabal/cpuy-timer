module dump();
	initial begin
		$dumpfile ("timer.vcd");
		$dumpvars (0, timer);
		#1;
	end
endmodule
