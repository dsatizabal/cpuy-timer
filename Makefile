# cocotb setup
MODULE = test.test_timer
export MODULE
TOPLEVEL = timer
VERILOG_SOURCES = timer.v

include $(shell cocotb-config --makefiles)/Makefile.sim

synth_timer:
	yosys -p "read_verilog timer.v; proc; opt; show -colors 2 -width -signed timer"

test_timer:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s tb -s dump -g2012 dump_timer.v timer.v tb.v
	PYTHONOPTIMIZE=${NOASSERT} vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

gtkwave_timer:
	gtkwave timer.vcd timer.gtkw

formal_timer:
	sby -f timer.sby
