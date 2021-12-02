package IntCode;

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Queue;

enum OpCodes {
	ADD(3),
	MULT(3),
	HALT(0);
	
	private int paramCount;
	
	OpCodes(int paramCount)
	{
		this.paramCount = paramCount;
	}
	
	public int getParamCount() {
		return paramCount;
	}
}


public class IntCode {
	
	// Interface for the table of opcodes
	private interface OpCodeMethods{
		int method();
	}
	
	// Memory is stored in a HashMap
	// This makes it expandable later
	private HashMap<Integer, Integer> memory;
	
	// The current IP is an integer
	private int ip;
	
	// Base for relative mode
	private int base;
	
	// Flags which tell the state of the machine
	private boolean paused, halted;
	
	// Input and output queues
	private Queue<Integer> input_queue, output_queue;
	
	// Can I make a call table?
	private OpCodeMethods[] opcodeFunctions = {
			this::add,
			this::mult
	};
	
	IntCode(int[] program, int ip){
		// Initialize the memory bank
		this.memory  = new HashMap<Integer, Integer>(program.length);
		
		// Transfer the program into memory
		for (int memloc=0; memloc < program.length; memloc++)
			this.memory.put(memloc, program[memloc]);
		
		// Set the IP
		this.ip = ip;
		
		// Initialize the input/output queues
		this.input_queue = new ArrayDeque<Integer>();
		this.output_queue = new ArrayDeque<Integer>();
		
	}
	
	// Sets a memory location
	public void set_memory_loc(int memloc, int value) {
		this.memory.replace(memloc, value);
	}
	
	// Push input to the queue
	public void setInput(int val) {
		this.input_queue.add(val);
	}
	
	// Get input from the queue
	private int getInput() {
		if (!this.input_queue.isEmpty())
			return this.input_queue.remove();
		return -1;
	}
	
	// Push output to the queue
	private void setOutput(int val) {
		this.output_queue.add(val);
	}
	
	// Get input from the queue
	public int getOutput() {
		if (!this.output_queue.isEmpty())
			return this.output_queue.remove();
		return -1;
	}
	
	private int add() {
		int first = this.memory.get(this.ip+1);
		int second = this.memory.get(this.ip+2);
		this.memory.replace(this.memory.get(this.ip+3), first+second);
		return this.ip+4;
	}
	
	private int mult() {
		int first = this.memory.get(this.ip+1);
		int second = this.memory.get(this.ip+2);
		this.memory.replace(this.memory.get(this.ip+3), first*second);
		return this.ip+4;
	}
	
	public int run() {
		// Are we halted? We're done
		if (this.halted) return -1;
		
		// Unpause
		this.paused = false;
		
		// Should we be halted?
		this.halted = ((this.ip == -1) ||						// The IP is -1 
					   (this.ip > this.memory.size()) || 		// The IP is off the end of memory
					   (this.memory.get(this.ip) == 99)); 		// We hit a stop opcode
		
		// Let's go!
		while ((this.ip < this.memory.size()) && !this.paused && !this.halted)
		{
			// Get the opcode
			int opcode = this.memory.get(this.ip);
			if (opcode == 99) {
				this.halted = true;
			} else {
				ip = this.opcodeFunctions[opcode].method();
			}
		}
		
		if (this.halted) return -1;
		return ip;
	}
	
}
