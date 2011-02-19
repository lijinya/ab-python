# -*- coding: utf-8 -*-
'''
Created on 2011-1-24

@author:whitefirer_
'''

import my_debugger

debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

list = debugger.enumerate_threads()

if list == False:
	print "enumerate_threads Something Wrong!"
	debugger.detach()
	exit()
	
for thread in list:
	thread_context = debugger.get_thread_context(thread)
	if thread_context == False:
		print "get_thread_context Something Wrong!"
		debugger.detach()
		exit()

	# Now let's output the contents of some of the registers
	print "[*] Dumping registers for thread ID: 0x%08x" % thread
	print "[**] EIP: 0x%08x" % thread_context.Eip
	print "[**] ESP: 0x%08x" % thread_context.Esp
	print "[**] EBP: 0x%08x" % thread_context.Ebp
	print "[**] EAX: 0x%08x" % thread_context.Eax
	print "[**] EBX: 0x%08x" % thread_context.Ebx
	print "[**] ECX: 0x%08x" % thread_context.Ecx
	print "[**] EDX: 0x%08x" % thread_context.Edx
	print "[*] END DUMP"

debugger.detach()

raw_input("Press Enter Key to exit...")

#end file