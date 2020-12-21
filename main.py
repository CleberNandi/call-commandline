# encoding: utf-8
from subprocess import Popen, PIPE
from typing import Any

class Cmd:
	def __init__(self, cmd:str) -> None:
		self.cmd = cmd
  
	def __call__(self, *args:Any) -> Any:
		command = f"{self.cmd} {' '.join(args)}"
		output = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
		return output.communicate()

class Command:
	def __getattr__(self, attribute:str) -> None:
		return Cmd(attribute)
	
if __name__ == "__main__":
	Command = Command()
	output, error = Command.dir()
	print(output.decode())