disk_a = [0]*20000
disk_b = [0]*30000

#Read/Write information to a block
def write_block(block_no, block_info):
	#Do something

def read_block(block_no, block_info):
	#Do something


#Create and delete disk
def create_disk(disk_id, num_blocks):
	#Do something

def delete_disk(disk_id):
	#Do something

def write_disk(id, block_no, block_info):
	#Do something

def read_disk(id, block_no, block_info):
	#Do something



# Only for 3.3
def checkpoint(id, no):
	#Do something

def rollback(id, checkpoint_no):
	#Do something