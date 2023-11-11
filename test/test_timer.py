import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

@cocotb.test()
async def normal_count_up_no_autoreload(dut):
    clock = Clock(dut.clk, 10, "us")
    cocotb.fork(clock.start())

    dut.enable.value = 1

    dut.direction.value = 1
    dut.auto_reload.value = 0
    dut.done_ack.value = 0
    dut.count.value = 65530
    dut.set.value = 1
    await ClockCycles(dut.clk, 5)
    dut.set.value = 0

    assert dut.done == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk, 20)

    assert dut.done == 1, f"Expected DONE";

@cocotb.test()
async def normal_count_down_no_autoreload(dut):
    clock = Clock(dut.clk, 10, "us")
    cocotb.fork(clock.start())

    dut.enable.value = 1

    dut.direction.value = 0
    dut.auto_reload.value = 0
    dut.done_ack.value = 0
    dut.count.value = 5
    dut.set.value = 1
    await ClockCycles(dut.clk, 5)
    dut.set.value = 0

    assert dut.done == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk, 20)

    assert dut.done == 1, f"Expected DONE";

@cocotb.test()
async def done_ack_no_autoreload(dut):
    clock = Clock(dut.clk, 10, "us")
    cocotb.fork(clock.start())

    dut.enable.value = 1

    dut.direction.value = 1
    dut.auto_reload.value = 0
    dut.done_ack.value = 0
    dut.count.value = 65530
    dut.set.value = 1
    await ClockCycles(dut.clk, 5)
    dut.set.value = 0

    assert dut.done == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk, 20)

    assert dut.done == 1, f"Expected DONE";

    dut.done_ack.value = 1
    await ClockCycles(dut.clk, 2)
    dut.done_ack.value = 0

    assert dut.done == 0, f"Expected NOT DONE (after ack)";

@cocotb.test()
async def count_up_with_autoreload(dut):
    clock = Clock(dut.clk, 10, "us")
    cocotb.fork(clock.start())

    dut.enable.value = 1

    dut.direction.value = 1
    dut.auto_reload.value = 1
    dut.done_ack.value = 0
    dut.count.value = 65530
    dut.set.value = 1
    await ClockCycles(dut.clk, 5)
    dut.set.value = 0

    assert dut.done == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk, 8)
    assert dut.done == 1, f"Expected DONE";

    dut.done_ack.value = 1
    await ClockCycles(dut.clk, 2)
    dut.done_ack.value = 0

    assert dut.done == 0, f"Expected NOT DONE ACK";
    await ClockCycles(dut.clk, 9)
    assert dut.done == 1, f"Expected AR DONE";

@cocotb.test()
async def count_down_with_autoreload(dut):
    clock = Clock(dut.clk, 10, "us")
    cocotb.fork(clock.start())

    dut.enable.value = 1

    dut.direction.value = 0
    dut.auto_reload.value = 1
    dut.done_ack.value = 0
    dut.count.value = 5
    dut.set.value = 1
    await ClockCycles(dut.clk, 5)
    dut.set.value = 0

    assert dut.done == 0, f"Expected NOT DONE";
    await ClockCycles(dut.clk, 7)
    assert dut.done == 1, f"Expected DONE";

    dut.done_ack.value = 1
    await ClockCycles(dut.clk, 2)
    dut.done_ack.value = 0

    assert dut.done == 0, f"Expected NOT DONE ACK";
    await ClockCycles(dut.clk, 7)
    assert dut.done == 1, f"Expected AR DONE";
