import mpi

rank= mpi.rank
if rank == 0:
   data = {'a': 7, 'b': 3.14}
   mpi.send(data,1)
   print ("Sending data from",rank,"data",data)
   data,status = mpi.recv(source=1)
   mpi.barrier()
   print ("Receving data at",rank,"data",data)
elif rank == 1:
   data1 = {'a': 7, 'b': 'abc'}
   mpi.send(data1,0)
   print ("Sending data from",rank,"data",data1)
   data,status = mpi.recv(source=0)
   mpi.barrier()
   print ("Recieving data at",rank,"data",data1)


