# Quantum Computing Project
## Description
This project is about making a small quantum search application and to 
make it run on a real quantum computer. The code builds a quantum
circuit, compile it in a way to be read by a quantum computer and
send it to a real machine. Real time evolution is displayed in the 
console.
## How to install
Before running it, one needs to create a python virtual environment 
and installed libraries via the following command.
```
pip install -r requirements.txt
```
The application requires a token from IBM to run. It can be obtained
by creating an account on their website.

https://quantum-computing.ibm.com/

Then the API token must be provided in the `.env` in order to make 
the application run.

## How to run

### Create an input file

The input file for the search is located in `files` and is a `.dimacs` format. For more information about `.dimacs` file
see below.

https://jix.github.io/varisat/manual/0.2.0/formats/dimacs.html

### Run the program

The command to run the application is the following.
```
python src/main.py
```

## How to test
If you want to contribute, don't forget to test the code while
developing.
```
python -m unittest
```