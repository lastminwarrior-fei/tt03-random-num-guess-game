import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def test_my_design(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())
    
    dut.rst.value = 1
    dut._log.info("reset") 
    await ClockCycles(dut.clk, 2)
    dut.rst.value = 0
    dut._log.info("result 0: " + str(dut.result.value))
    
    dut.guess.value = 0b000000
    dut._log.info("guess 1: " + str(dut.guess.value))
    await ClockCycles(dut.clk, 2)
    dut._log.info("result 1: " + str(dut.result.value)) 
    
    dut.guess.value = 0b000001
    dut._log.info("guess 2: " + str(dut.guess.value))
    await ClockCycles(dut.clk, 2)
    dut._log.info("result 2: " + str(dut.result.value)) 
    
    dut.guess.value = 0b000011
    dut._log.info("guess 3: " + str(dut.guess.value))
    await ClockCycles(dut.clk, 2)
    dut._log.info("result 3: " + str(dut.result.value)) 
    
    dut.guess.value = 0b000000
    dut._log.info("guess 4: " + str(dut.guess.value))
    await ClockCycles(dut.clk, 2)
    dut._log.info("result 4: " + str(dut.result.value)) 
    
    dut.guess.value = 0b000000
    dut._log.info("guess 5: " + str(dut.guess.value))
    await ClockCycles(dut.clk, 2)
    dut._log.info("result 5: " + str(dut.result.value)) 
