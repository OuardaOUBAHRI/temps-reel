import datetime
import time
import threading


stop_thread = False
tank= []


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task(threading.Thread):


	name = None
	period = None
	execution_time = None


    	############################################################################
	def __init__(self, name, period, execution_time, fifo_write = 0):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.fifo_write = fifo_write
		
		threading.Thread.__init__(self)

    	############################################################################
	def run(self):

		global tank

		while(not stop_thread):
				
			print(self.name + " : Starting task")
			
			for i in range (self.fifo_write) :
				tank.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
            
				
    
			print(len(tank))
			##else :
				##while (len(tank) > 0 and len(tank) < 50 ):
					##print(self.name + " : " + tank[0])
					##del tank[0]	


			
			time.sleep(self.execution_time)
			print(self.name + " : Stopping task")
			time.sleep(self.period - self.execution_time)




	
####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


	task_list = []

	# Instanciation of task objects

	task_list.append(my_task(name="pump_1", period=5, execution_time=2, fifo_write=10))
	task_list.append(my_task(name="pump_2", period=15, execution_time=3, fifo_write=20))
	##task_list.append(my_task(name="machine_1", period=5, execution_time=5))
	##task_list.append(my_task(name="machine_2", period=5, execution_time=3))
	


	for current_task in task_list :
		current_task.start()










