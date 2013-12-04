CMPE272-Extra-assingment
========================

CMPE272 Extra Assignment for pyMPI

 I have completed my extra credit assignment of topic:

 Use pyMPI to implement a parallel program in python using MPI which send receives messages in parallel.http://pympi.sourceforge.net/ 

I have attached my code and print-screens of code being executed.
Send you two print-screens for execution execution  :

1. With mpi.barrier()
2. Without mpi.barrier() function.

Tutorial: 

Pre-requisites:
Python (which will be already installed in most cases)
  
     $sudo apt-get install python

Install openMPI using command:
  
     $sudo apt-get libopenmpi-dev
or
  
     $sudo apt-get libopenmpi1.5-dev

Now download pyMPI package to work with python from http://sourceforge.net/projects/pympi/files/latest/download

Extract the archive:

  
     $tar -xvf pyMPI-2.5b0.tar.gz

Write your python code for MPI and save as msg.py:

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

Save the code in same folder as pyMPI and run:

  
     $ mpirun -np 2 pyMPI msg.py

You can also use Synaptic Package Manager for installation:
Install Synaptic Package Manager:

     $sudo apt-get install synaptic

Open Synaptic GUI tool, now directly search and select all the packages to be installed.



Nishant Ajay Mehta
smarts3.in
nishant.a.m@gmail.com
