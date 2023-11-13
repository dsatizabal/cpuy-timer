import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles


@cocotb.test()
async def normal_count_up_no_autoreload(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1

    dut.direction_tb.value = 1
    dut.auto_reload_tb.value = 0
    dut.done_ack_tb.value = 0
    dut.count_tb.value = 65531 # Counts 5, transition from FFFFh to 0 counts
    dut.set_tb.value = 1
    await ClockCycles(dut.clk_tb, 5)
    dut.set_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE";

    await ClockCycles(dut.clk_tb, 6)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected DONE";

@cocotb.test()
async def normal_count_down_no_autoreload(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1

    dut.direction_tb.value = 0
    dut.auto_reload_tb.value = 0
    dut.done_ack_tb.value = 0
    dut.count_tb.value = 5
    dut.set_tb.value = 1
    await ClockCycles(dut.clk_tb, 5)
    dut.set_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk_tb, 6)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected DONE";

@cocotb.test()
async def done_ack_no_autoreload(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1

    dut.direction_tb.value = 1
    dut.auto_reload_tb.value = 0
    dut.done_ack_tb.value = 0
    dut.count_tb.value = 65531
    dut.set_tb.value = 1
    await ClockCycles(dut.clk_tb, 5)
    dut.set_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk_tb, 6)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected DONE";

    dut.done_ack_tb.value = 1
    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.done_ack_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE (after ack)";

@cocotb.test()
async def count_up_with_autoreload(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1

    dut.direction_tb.value = 1
    dut.auto_reload_tb.value = 1
    dut.done_ack_tb.value = 0
    dut.count_tb.value = 65531
    dut.set_tb.value = 1
    await ClockCycles(dut.clk_tb, 5)
    dut.set_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk_tb, 6)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected DONE";

    dut.done_ack_tb.value = 1
    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.done_ack_tb.value = 0
    assert dut.done_tb == 0, f"Expected NOT DONE ACK";

    await ClockCycles(dut.clk_tb, 5)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected AR DONE";

@cocotb.test()
async def count_down_with_autoreload(dut):
    clock = Clock(dut.clk_tb, 10, "us")
    cocotb.fork(clock.start())

    dut.enable_tb.value = 1

    dut.direction_tb.value = 0
    dut.auto_reload_tb.value = 1
    dut.done_ack_tb.value = 0
    dut.count_tb.value = 5
    dut.set_tb.value = 1
    await ClockCycles(dut.clk_tb, 5)
    dut.set_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE";

    await ClockCycles(dut.clk_tb, 6)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");

    assert dut.done_tb == 1, f"Expected DONE";

    dut.done_ack_tb.value = 1
    await ClockCycles(dut.clk_tb, 1)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    dut.done_ack_tb.value = 0

    assert dut.done_tb == 0, f"Expected NOT DONE ACK";
    await ClockCycles(dut.clk_tb, 5)
    # Required to have the propper results (propagation?), otherwise we'd require an additional clk cycle
    await Timer(10, units="ns");
    assert dut.done_tb == 1, f"Expected AR DONE";
