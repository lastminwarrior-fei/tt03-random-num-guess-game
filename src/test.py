import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_my_design(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())
    
    dut.guess.value = 0b000000
    dut.rst.value = 1 
    await ClockCycles(dut.clk, 1)
    dut.rst.value = 0
    dut._log.info("reset")
    
    dut.guess.value = 0b000000
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 0: " + str(dut.result.value))
    dut._log.info("guess 1: " + str(dut.guess.value))
    
    dut.guess.value = 0b000001
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 1: " + str(dut.result.value))
    dut._log.info("guess 2: " + str(dut.guess.value))
    
    dut.guess.value = 0b000011
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 2: " + str(dut.result.value)) 
    dut._log.info("guess 3: " + str(dut.guess.value))
    
    dut.guess.value = 0b000000
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 3: " + str(dut.result.value))
    dut._log.info("guess 4: " + str(dut.guess.value))
    
    dut.guess.value = 0b000000
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 4: " + str(dut.result.value))
    dut._log.info("guess 5: " + str(dut.guess.value))
    
    await ClockCycles(dut.clk, 1)
    dut._log.info("result 5: " + str(dut.result.value)) 
