import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_my_design(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())
    
    dut.rst.value = 1
    await ClockCycles(dut.clk, 5)
    dut.rst = 0
    assert dut.result.value == 0b000000
    dut._log.info("test0 passed")
