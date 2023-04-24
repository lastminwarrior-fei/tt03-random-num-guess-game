import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_my_design(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())
    
    dut.rst.value = 1
    await ClockCycles(dut.clk, 2)
    dut.rst = 0
    assert dut.result.value == 0b000000
    dut._log.info("reset test passed")
    
    dut.guess.value = 0b000000
    dut._log.info("guess 1: ", dut.guess.value)
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 1: ", dut.result.value) 
    
    dut.guess.value = 0b000001
    dut._log.info("guess 2: ", dut.guess.value)
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 2: ", dut.result.value) 
    
    dut.guess.value = 0b000011
    dut._log.info("guess 3: ", dut.guess.value)
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 3: ", dut.result.value) 
    
    dut.guess.value = 0b000000
    dut._log.info("guess 4: ", dut.guess.value)
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 4: ", dut.result.value) 
    
    dut.guess.value = 0b000000
    dut._log.info("guess 5: ", dut.guess.value)
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 5: ", dut.result.value) 
