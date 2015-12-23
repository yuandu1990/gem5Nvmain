# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Steve Reinhardt

# Simple test script
#
# "m5 test.py"

import optparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath, fatal

addToPath('../common')
addToPath('../ruby')

import Options
import Ruby
import Simulation
import CacheConfig
import MemConfig
from Caches import *
from cpu2000 import *
import cpu2006

# Get paths we might need.  It's expected this file is in m5/configs/example.
config_path = os.path.dirname(os.path.abspath(__file__))
print config_path   # 'configs/cpu2006'
config_root = os.path.dirname(config_path)
print config_root
m5_root = os.path.dirname(config_root)
print m5_root

def get_processes(options):
    """Interprets provided options and returns a list of processes"""

    multiprocesses = []
    inputs = []
    outputs = []
    errouts = []
    pargs = []

    workloads = options.cmd.split(';')
    if options.input != "":
        inputs = options.input.split(';')
    if options.output != "":
        outputs = options.output.split(';')
    if options.errout != "":
        errouts = options.errout.split(';')
    if options.options != "":
        pargs = options.options.split(';')

    idx = 0
    for wrkld in workloads:
        process = LiveProcess()
        process.executable = wrkld
        process.cwd = os.getcwd()

        if len(pargs) > idx:
            process.cmd = [wrkld] + pargs[idx].split()
        else:
            process.cmd = [wrkld]

        if len(inputs) > idx:
            process.input = inputs[idx]
        if len(outputs) > idx:
            process.output = outputs[idx]
        if len(errouts) > idx:
            process.errout = errouts[idx]

        multiprocesses.append(process)
        idx += 1

    if options.smt:
        assert(options.cpu_type == "detailed" or options.cpu_type == "inorder")
        return multiprocesses, idx
    else:
        return multiprocesses, 1


parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)

# Benchmark options

parser.add_option("-b", "--benchmark", default="",
                 help="The benchmark to be loaded.")

parser.add_option("--chkpt", default="",
                 help="The checkpoint to load.")

execfile(os.path.join(config_root, "common", "Options.py"))

if '--ruby' in sys.argv:
    Ruby.define_options(parser)

(options, args) = parser.parse_args()

if args:
    print "Error: script doesn't take any positional arguments"
    sys.exit(1)

benchmarkprocesses = []
workloads = options.benchmark.split(';')
for wrkld in workloads:
	if wrkld == 'perlbench':
		benchmarkprocesses.append(cpu2006.perlbench)
	if wrkld == 'bzip2':
		benchmarkprocesses.append(cpu2006.bzip2)
	if wrkld == 'bzip21':
		benchmarkprocesses.append(cpu2006.bzip21)
	if wrkld == 'bzip22':
		benchmarkprocesses.append(cpu2006.bzip22)
	if wrkld == 'bzip23':
		benchmarkprocesses.append(cpu2006.bzip23)
	if wrkld == 'bzip24':
		benchmarkprocesses.append(cpu2006.bzip24)
	if wrkld == 'bzip25':
		benchmarkprocesses.append(cpu2006.bzip25)
	if wrkld == 'bzip26':
		benchmarkprocesses.append(cpu2006.bzip26)
	if wrkld == 'bzip27':
		benchmarkprocesses.append(cpu2006.bzip27)
	if wrkld == 'gcc':
		benchmarkprocesses.append(cpu2006.gcc)
	if wrkld == 'bwaves':
		benchmarkprocesses.append(cpu2006.bwaves)
	if wrkld == 'gamess':
		benchmarkprocesses.append(cpu2006.gamess)
	if wrkld == 'mcf':
		benchmarkprocesses.append(cpu2006.mcf)
	if wrkld == 'mcf1':
		benchmarkprocesses.append(cpu2006.mcf1)
	if wrkld == 'mcf2':
		benchmarkprocesses.append(cpu2006.mcf2)
	if wrkld == 'mcf3':
		benchmarkprocesses.append(cpu2006.mcf3)
	if wrkld == 'mcf4':
		benchmarkprocesses.append(cpu2006.mcf4)
	if wrkld == 'mcf5':
		benchmarkprocesses.append(cpu2006.mcf5)
	if wrkld == 'mcf6':
		benchmarkprocesses.append(cpu2006.mcf6)
	if wrkld == 'mcf7':
		benchmarkprocesses.append(cpu2006.mcf7)
	if wrkld == 'milc':
		benchmarkprocesses.append(cpu2006.milc)
	if wrkld == 'milc1':
		benchmarkprocesses.append(cpu2006.milc1)
	if wrkld == 'milc2':
		benchmarkprocesses.append(cpu2006.milc2)
	if wrkld == 'milc3':
		benchmarkprocesses.append(cpu2006.milc3)	
	if wrkld == 'zeusmp':
		benchmarkprocesses.append(cpu2006.zeusmp)
	if wrkld == 'gromacs':
		benchmarkprocesses.append(cpu2006.gromacs)
	if wrkld == 'gromacs1':
		benchmarkprocesses.append(cpu2006.gromacs1)
	if wrkld == 'gromacs2':
		benchmarkprocesses.append(cpu2006.gromacs2)
	if wrkld == 'gromacs3':
		benchmarkprocesses.append(cpu2006.gromacs3)					
	if wrkld == 'cactusADM':
		benchmarkprocesses.append(cpu2006.cactusADM)
	if wrkld == 'leslie3d':
		benchmarkprocesses.append(cpu2006.leslie3d)
	if wrkld == 'leslie3d1':
		benchmarkprocesses.append(cpu2006.leslie3d1)
	if wrkld == 'leslie3d2':
		benchmarkprocesses.append(cpu2006.leslie3d2)
	if wrkld == 'leslie3d3':
		benchmarkprocesses.append(cpu2006.leslie3d3)
	if wrkld == 'namd':
		benchmarkprocesses.append(cpu2006.namd)
	if wrkld == 'gobmk':
		benchmarkprocesses.append(cpu2006.gobmk)
	if wrkld == 'dealII':
	   benchmarkprocesses.append(cpu2006.dealII)
	if wrkld == 'soplex':
	   benchmarkprocesses.append(cpu2006.soplex)
	if wrkld == 'povray':
	   benchmarkprocesses.append(cpu2006.povray)
	if wrkld == 'calculix':
	   benchmarkprocesses.append(cpu2006.calculix)
	if wrkld == 'hmmer':
	   benchmarkprocesses.append(cpu2006.hmmer)
	if wrkld == 'sjeng':
	   benchmarkprocesses.append(cpu2006.sjeng)
	if wrkld == 'GemsFDTD':
	   benchmarkprocesses.append(cpu2006.GemsFDTD)
	if wrkld == 'libquantum':
	   benchmarkprocesses.append(cpu2006.libquantum)
	if wrkld == 'h264ref':
	   benchmarkprocesses.append(cpu2006.h264ref)
	if wrkld == 'tonto':
	   benchmarkprocesses.append(cpu2006.tonto)
	if wrkld == 'lbm':
	   benchmarkprocesses.append(cpu2006.lbm)
	if wrkld == 'omnetpp':
	   benchmarkprocesses.append(cpu2006.omnetpp)
	if wrkld == 'astar':
	   benchmarkprocesses.append(cpu2006.astar)
	if wrkld == 'wrf':
	   benchmarkprocesses.append(cpu2006.wrf)
	if wrkld == 'sphinx3':
	   benchmarkprocesses.append(cpu2006.sphinx3)
	if wrkld == 'xalancbmk':
	   benchmarkprocesses.append(cpu2006.xalancbmk)
	if wrkld == 'specrand_i':
	   benchmarkprocesses.append(cpu2006.specrand_i)
	if wrkld == 'specrand_f':
	   benchmarkprocesses.append(cpu2006.specrand_f)


multiprocesses = []
numThreads = 1

if options.bench:
    apps = options.bench.split("-")
    if len(apps) != options.num_cpus:
        print "number of benchmarks not equal to set num_cpus!"
        sys.exit(1)

    for app in apps:
        try:
            if buildEnv['TARGET_ISA'] == 'alpha':
                exec("workload = %s('alpha', 'tru64', '%s')" % (
                        app, options.spec_input))
            elif buildEnv['TARGET_ISA'] == 'arm':
                exec("workload = %s('arm_%s', 'linux', '%s')" % (
                        app, options.arm_iset, options.spec_input))
            else:
                exec("workload = %s(buildEnv['TARGET_ISA', 'linux', '%s')" % (
                        app, options.spec_input))
            multiprocesses.append(workload.makeLiveProcess())
        except:
            print >>sys.stderr, "Unable to find workload for %s: %s" % (
                    buildEnv['TARGET_ISA'], app)
            sys.exit(1)
elif options.cmd:
    multiprocesses, numThreads = get_processes(options)
#else:
#    print >> sys.stderr, "No workload specified. Exiting!\n"
#    sys.exit(1)

for bench in benchmarkprocesses:
	multiprocesses.append(bench)

(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if options.smt and options.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = options.num_cpus
#light
#system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
#               mem_mode = test_mem_mode,
#               mem_ranges = [AddrRange(options.mem_size)],
#               cache_line_size = options.cacheline_size)
system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
                mem_mode = test_mem_mode,
                mem_ranges = [AddrRange(options.nvmain_start,options.nvmain_end),
		AddrRange(options.dram_start,options.dram_end)],
                cache_line_size = options.cacheline_size)
#end
# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
                                   voltage_domain = system.voltage_domain)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
                                       voltage_domain =
                                       system.cpu_voltage_domain)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

# Sanity check
if options.fastmem:
    if CPUClass != AtomicSimpleCPU:
        fatal("Fastmem can only be used with atomic CPU!")
    if (options.caches or options.l2cache):
        fatal("You cannot use fastmem in combination with caches!")

if options.simpoint_profile:
    if not options.fastmem:
        # Atomic CPU checked with fastmem option already
        fatal("SimPoint generation should be done with atomic cpu and fastmem")
    if np > 1:
        fatal("SimPoint generation not supported with more than one CPUs")

for i in xrange(np):
    if options.smt:
       system.cpu[i].workload = multiprocesses
    elif len(multiprocesses) == 1:
       system.cpu[i].workload = multiprocesses[0]
    else:
        system.cpu[i].workload = multiprocesses[i]

    if options.fastmem:
       system.cpu[i].fastmem = True

    if options.simpoint_profile:
       system.cpu[i].addSimPointProbe(options.simpoint_interval)

    if options.checker:
       system.cpu[i].addCheckerCpu()

    #system.cpu[i].workload = process[i]
    system.cpu[i].createThreads()

if options.ruby:
    if not (options.cpu_type == "detailed" or options.cpu_type == "timing"):
        print >> sys.stderr, "Ruby requires TimingSimpleCPU or O3CPU!!"
        sys.exit(1)

    # Use SimpleMemory with the null option since this memory is only used
    # for determining which addresses are within the range of the memory.
    # No space allocation is required.
#light
    #system.physmem = SimpleMemory(range=AddrRange(options.mem_size),
    #                          null = True)
    system.physmem = SimpleMemory(range=AddrRange(options.nvm_end),
                              null = True)
#end
    options.use_map = True
    Ruby.create_system(options, system)
    assert(options.num_cpus == len(system.ruby._cpu_ports))

    system.ruby.clk_domain = SrcClockDomain(clock = options.ruby_clock,
                                        voltage_domain = system.voltage_domain)
    for i in xrange(np):
        ruby_port = system.ruby._cpu_ports[i]

        # Create the interrupt controller and connect its ports to Ruby
        # Note that the interrupt controller is always present but only
        # in x86 does it have message ports that need to be connected
        system.cpu[i].createInterruptController()

        # Connect the cpu's cache ports to Ruby
        system.cpu[i].icache_port = ruby_port.slave
        system.cpu[i].dcache_port = ruby_port.slave
        if buildEnv['TARGET_ISA'] == 'x86':
            system.cpu[i].interrupts.pio = ruby_port.master
            system.cpu[i].interrupts.int_master = ruby_port.slave
            system.cpu[i].interrupts.int_slave = ruby_port.master
            system.cpu[i].itb.walker.port = ruby_port.slave
            system.cpu[i].dtb.walker.port = ruby_port.slave
else:
    MemClass = Simulation.setMemClass(options)
    system.membus = CoherentXBar()
 #   system.membus = XBarControl(num_of_sets = options.num_of_sets)
    system.system_port = system.membus.slave
    CacheConfig.config_cache(options, system)
    MemConfig.config_mem(options, system)

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)