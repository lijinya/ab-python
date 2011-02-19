# -*- coding: utf-8 -*-
'''
Created on 2011-1-24
Option: Maybe the function pointer is no very safe
@author: whitefirer_
'''

from ctypes import *

# Let's map the Microsoft types to ctypes for clarity
WORD		= c_ushort
DWORD		= c_ulong
LONG		= c_long
BYTE		= c_ubyte
LPBYTE		= POINTER(c_ubyte)
LPTSTR		= POINTER(c_char)
LPSTR		= POINTER(c_char)
HANDLE		= c_void_p
LPVOID		= c_void_p
PVOID		= c_void_p
ULONG_PTR	= c_ulong
LPTHREAD_START_ROUTINE = c_void_p

# Constants
DEBUG_PROCESS		= 0x00000001
CREATE_NEW_CONSOLE	= 0x00000010

DELETE			= 0x00010000L
READ_CONTROL	= 0x00020000L
WRITE_DAC		= 0x00040000L
WRITE_OWNER		= 0x00080000L
SYNCHRONIZE		= 0x00100000L

STANDARD_RIGHTS_REQUIRED	= 0x000F0000L
STANDARD_RIGHTS_READ		= READ_CONTROL
STANDARD_RIGHTS_WRITE		= READ_CONTROL
STANDARD_RIGHTS_EXECUTE		= READ_CONTROL

STANDARD_RIGHTS_ALL = 0x001F0000L

SPECIFIC_RIGHTS_ALL = 0x0000FFFFL

PROCESS_TERMINATE			= 0x0001
PROCESS_CREATE_THREAD		= 0x0002
PROCESS_SET_SESSIONID		= 0x0004
PROCESS_VM_OPERATION		= 0x0008
PROCESS_VM_READ				= 0x0010
PROCESS_VM_WRITE			= 0x0020
PROCESS_DUP_HANDLE			= 0x0040
PROCESS_CREATE_PROCESS		= 0x0080
PROCESS_SET_QUOTA			= 0x0100
PROCESS_SET_INFORMATION		= 0x0200
PROCESS_QUERY_INFORMATION	= 0x0400
PROCESS_SUSPEND_RESUME		= 0x0800
PROCESS_ALL_ACCESS			= STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF

THREAD_TERMINATE			= 0x0001
THREAD_SUSPEND_RESUME		= 0x0002
THREAD_GET_CONTEXT			= 0x0008
THREAD_SET_CONTEXT			= 0x0010
THREAD_SET_INFORMATION		= 0x0020
THREAD_QUERY_INFORMATION	= 0x0040
THREAD_SET_THREAD_TOKEN		= 0x0080
THREAD_IMPERSONATE			= 0x0100
THREAD_DIRECT_IMPERSONATION	= 0x0200
THREAD_ALL_ACCESS			= (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x3FF)

STATUS_WAIT_0					= 0x00000000L
STATUS_ABANDONED_WAIT_0			= 0x00000080L
STATUS_USER_APC					= 0x000000C0L
STATUS_TIMEOUT					= 0x00000102L
STATUS_PENDING					= 0x00000103L
DBG_EXCEPTION_HANDLED			= 0x00010001L
DBG_CONTINUE					= 0x00010002L
STATUS_SEGMENT_NOTIFICATION		= 0x40000005L
DBG_TERMINATE_THREAD			= 0x40010003L
DBG_TERMINATE_PROCESS			= 0x40010004L
DBG_CONTROL_C					= 0x40010005L
DBG_CONTROL_BREAK				= 0x40010008L
DBG_COMMAND_EXCEPTION			= 0x40010009L
STATUS_GUARD_PAGE_VIOLATION		= 0x80000001L
STATUS_DATATYPE_MISALIGNMENT	= 0x80000002L
STATUS_BREAKPOINT				= 0x80000003L
STATUS_SINGLE_STEP				= 0x80000004L
DBG_EXCEPTION_NOT_HANDLED		= 0x80010001L
STATUS_ACCESS_VIOLATION			= 0xC0000005L
STATUS_IN_PAGE_ERROR			= 0xC0000006L
STATUS_INVALID_HANDLE			= 0xC0000008L
STATUS_NO_MEMORY				= 0xC0000017L
STATUS_ILLEGAL_INSTRUCTION		= 0xC000001DL
STATUS_NONCONTINUABLE_EXCEPTION	= 0xC0000025L
STATUS_INVALID_DISPOSITION		= 0xC0000026L
STATUS_ARRAY_BOUNDS_EXCEEDED	= 0xC000008CL
STATUS_FLOAT_DENORMAL_OPERAND	= 0xC000008DL
STATUS_FLOAT_DIVIDE_BY_ZERO		= 0xC000008EL
STATUS_FLOAT_INEXACT_RESULT		= 0xC000008FL
STATUS_FLOAT_INVALID_OPERATION	= 0xC0000090L
STATUS_FLOAT_OVERFLOW			= 0xC0000091L
STATUS_FLOAT_STACK_CHECK		= 0xC0000092L
STATUS_FLOAT_UNDERFLOW			= 0xC0000093L
STATUS_INTEGER_DIVIDE_BY_ZERO	= 0xC0000094L
STATUS_INTEGER_OVERFLOW			= 0xC0000095L
STATUS_PRIVILEGED_INSTRUCTION	= 0xC0000096L
STATUS_STACK_OVERFLOW			= 0xC00000FDL
STATUS_CONTROL_C_EXIT			= 0xC000013AL
STATUS_FLOAT_MULTIPLE_FAULTS	= 0xC00002B4L
STATUS_FLOAT_MULTIPLE_TRAPS		= 0xC00002B5L
STATUS_REG_NAT_CONSUMPTION		= 0xC00002C9L

IGNORE		= 0				# Ignore signal
INFINITE	= 0xFFFFFFFF	# Infinite timeout

# Structures for CreateProcessA() function
class STARTUPINFO(Structure):
	_fields_ = [
		("cb", DWORD),
		("lpReserved", LPTSTR),
		("lpDesktop", LPTSTR),
		("lpTitle", LPTSTR),
		("dwX", DWORD),
		("dwY", DWORD),
		("dwXSize", DWORD),
		("dwYSize", DWORD),
		("dwXCountChars", DWORD),
		("dwYCountChars", DWORD),
		("dwFillAttribute",DWORD),
		("dwFlags", DWORD),
		("wShowWindow", WORD),
		("cbReserved2", WORD),
		("lpReserved2", LPBYTE),
		("hStdInput", HANDLE),
		("hStdOutput", HANDLE),
		("hStdError", HANDLE),
	]
	
class PROCESS_INFORMATION(Structure):
	_fields_ = [
		("hProcess", HANDLE),
		("hThread", HANDLE),
		("dwProcessId", DWORD),
		("dwThreadId", DWORD),
	]
	
EXCEPTION_NONCONTINUABLE		= 0x1	# Noncontinuable exception
EXCEPTION_MAXIMUM_PARAMETERS	= 15	# maximum number of exception parameters

class EXCEPTION_RECORD(Structure):
	_fields_ = [
		("ExceptionCode", DWORD),
		("EceptionFlags", DWORD),
		("ExceptionRecord", PVOID),#EXCEPTION_RECORD
		("ExceptionAddress", PVOID),
		("NumberParameters", DWORD),
		("ExceptionInformation", ULONG_PTR * EXCEPTION_MAXIMUM_PARAMETERS)
	]
	
EXCEPTION_DEBUG_EVENT		= 1
CREATE_THREAD_DEBUG_EVENT	= 2
CREATE_PROCESS_DEBUG_EVENT	= 3
EXIT_THREAD_DEBUG_EVENT		= 4
EXIT_PROCESS_DEBUG_EVENT	= 5
LOAD_DLL_DEBUG_EVENT		= 6
UNLOAD_DLL_DEBUG_EVENT		= 7
OUTPUT_DEBUG_STRING_EVENT	= 8
RIP_EVENT					= 9

class EXCEPTION_DEBUG_INFO(Structure):
	_fields_ = [
		("ExceptionRecord", EXCEPTION_RECORD),
		("dwFirstChance", DWORD)
	]

class CREATE_THREAD_DEBUG_INFO(Structure):
	_fields_ = [
		("hThread", HANDLE),
		("lpThreadLocalBase", LPVOID),
		("lpStartAddress", LPTHREAD_START_ROUTINE)
	]

class CREATE_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [
		("hFile", HANDLE),
		("hProcess", HANDLE),
		("hThread", HANDLE),
		("lpBaseOfImage", LPVOID),
		("dwDebugInfoFileOffset", DWORD),
		("nDebugInfoSize", DWORD),
		("lpThreadLocalBase", LPVOID),
		("lpStartAddress", LPTHREAD_START_ROUTINE),
		("fUnicode", WORD)
	]

class EXIT_PROCESS_DEBUG_INFO(Structure):
	_fields_ = [
		("dwExitCode", DWORD)
	]

class EXIT_THREAD_DEBUG_INFO(Structure):
	_fields_ = [
		("dwExitCode", DWORD)
	]
class LOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [
		("hFile", HANDLE),
		("lpBaseOfDll", LPVOID),
		("dwDebugInfoFileOffset", DWORD),
		("nDebugInfoSize", DWORD),
		("lpImageName", LPVOID),
		("fUnicode", WORD)
	]

class UNLOAD_DLL_DEBUG_INFO(Structure):
	_fields_ = [
		("lpBaseOfDll", LPVOID)
	]

class OUTPUT_DEBUG_STRING_INFO(Structure):
	_fields_ = [
		("lpDebugStringData", LPSTR),
		("fUnicode", WORD),
		("nDebugStringLength", WORD)
	]

class RIP_INFO(Structure):
	_fields_ = [
		("dwError", DWORD),
		("dwType", DWORD)
	]
	
class U(Union):
	_fields_ = [
		("Exception", EXCEPTION_DEBUG_INFO),
		("CreateThread", CREATE_THREAD_DEBUG_INFO),
		("CreateProcessInfo", CREATE_PROCESS_DEBUG_INFO),
		("ExitThread", EXIT_THREAD_DEBUG_INFO),
		("ExitProcess", EXIT_PROCESS_DEBUG_INFO),
		("LoadDll", LOAD_DLL_DEBUG_INFO),
		("UnloadDll", UNLOAD_DLL_DEBUG_INFO),
		("DebugString", OUTPUT_DEBUG_STRING_INFO),
		("RipInfo", RIP_INFO)
	]
	
class DEBUG_EVENT(Structure):
	_fields_ = [
		("dwDebugEventCode", DWORD),
		("dwProcessId", DWORD),
		("dwThreadId", DWORD),
		("u", U)
	]

class THREADENTRY32(Structure):
	_fields_ = [
		("dwSize", DWORD),
		("cntUsage", DWORD),
		("th32ThreadID", DWORD),
		("th32OwnerProcessID", DWORD),
		("tpBasePri", LONG),
		("tpDeltaPri", LONG),
		("dwFlags", DWORD)
	]
	
EXCEPTION_READ_FAULT		= 0 # Access violation was caused by a read
EXCEPTION_WRITE_FAULT		= 1 # Access violation was caused by a write
EXCEPTION_EXECUTE_FAULT		= 8 # Access violation was caused by an instruction fetch
	
CONTEXT_i386	= 0x00010000	# this assumes that i386 and
CONTEXT_i486	= 0x00010000	# i486 have identical context records

# end_wx86

CONTEXT_CONTROL			= (CONTEXT_i386 | 0x00000001L) # SS:SP, CS:IP, FLAGS, BP
CONTEXT_INTEGER			= (CONTEXT_i386 | 0x00000002L) # AX, BX, CX, DX, SI, DI
CONTEXT_SEGMENTS		= (CONTEXT_i386 | 0x00000004L) # DS, ES, FS, GS
CONTEXT_FLOATING_POINT	= (CONTEXT_i386 | 0x00000008L) # 387 state
CONTEXT_DEBUG_REGISTERS	= (CONTEXT_i386 | 0x00000010L) # DB 0-3,6,7
CONTEXT_EXTENDED_REGISTERS	= (CONTEXT_i386 | 0x00000020L) # cpu specific extensions

CONTEXT_FULL = (CONTEXT_CONTROL | CONTEXT_INTEGER |\
			CONTEXT_SEGMENTS)

CONTEXT_ALL = (CONTEXT_CONTROL | CONTEXT_INTEGER |\
			CONTEXT_SEGMENTS | CONTEXT_FLOATING_POINT |\
			CONTEXT_DEBUG_REGISTERS | CONTEXT_EXTENDED_REGISTERS)
MAXIMUM_SUPPORTED_EXTENSION	= 512
SIZE_OF_80387_REGISTERS		= 80

class FLOATING_SAVE_AREA(Structure):
	_fields_ = [
		("ControlWord", DWORD),
		("StatusWord", DWORD),
		("TagWord", DWORD),
		("ErrorOffset", DWORD),
		("ErrorSelector", DWORD),
		("DataOffset", DWORD),
		("DataSelector", DWORD),
		("RegisterArea", BYTE * SIZE_OF_80387_REGISTERS),
		("Cr0NpxState", DWORD),	
	]

class CONTEXT(Structure):
	_fields_ = [
		("ContextFlags", DWORD),
		("Dr0", DWORD),
		("Dr1", DWORD),
		("Dr2", DWORD),
		("Dr3", DWORD),
		("Dr6", DWORD),
		("Dr7", DWORD),
		("FloatSave", FLOATING_SAVE_AREA),
		("SegGs", DWORD),
		("SegFs", DWORD),
		("SegEs", DWORD),
		("SegDs", DWORD),
		("Edi", DWORD),
		("Esi", DWORD),
		("Ebx", DWORD),
		("Edx", DWORD),
		("Ecx", DWORD),
		("Eax", DWORD),
		("Ebp", DWORD),
		("Eip", DWORD),
		("SegCs", DWORD),
		("EFlags", DWORD),	
		("Esp", DWORD),
		("SegSs", DWORD),
		("ExtendedRegisters", BYTE * MAXIMUM_SUPPORTED_EXTENSION)
	]

TH32CS_SNAPHEAPLIST	= 0x00000001
TH32CS_SNAPPROCESS	= 0x00000002
TH32CS_SNAPTHREAD	= 0x00000004
TH32CS_SNAPMODULE	= 0x00000008
TH32CS_SNAPMODULE32	= 0x00000010
TH32CS_SNAPALL		= (TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE)
TH32CS_INHERIT		= 0x80000000

#endfile