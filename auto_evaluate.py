import subprocess

def run_cpp_with_input(cpp_file, input_text):
    # Compile the C++ code
    compilation_process = subprocess.run(['g++', cpp_file, '-o', 'program'], capture_output=True, text=True)
    
    # Check if compilation was successful
    if compilation_process.returncode != 0:
        print("Compilation failed:")
        print(compilation_process.stderr)
        return
    
    # Run the compiled program with input text
    execution_process = subprocess.run(['./program'], input=input_text, capture_output=True, text=True)
    
    # Check if execution was successful
    if execution_process.returncode != 0:
        print("Execution failed:")
        print(execution_process.stderr)
        return
    
    # Return the output of the program
    return execution_process.stdout

def run_python_with_input(py_file, input_text):

    # Run the Python script with input text
    execution_process = subprocess.run(['python', py_file], input=input_text, capture_output=True, text=True)
    
    # Check if execution was successful
    if execution_process.returncode != 0:
        print("Execution failed:")
        print(execution_process.stderr)
        return
    
    # Return the output of the program
    return execution_process.stdout

def run_c_with_input(c_file, input_text):
    # Compile the C code
    compilation_process = subprocess.run(['gcc', c_file, '-o', 'program'], capture_output=True, text=True)
    
    # Check if compilation was successful
    if compilation_process.returncode != 0:
        print("Compilation failed:")
        print(compilation_process.stderr)
        return

    # Run the compiled program with input text
    execution_process = subprocess.run(['./program'], input=input_text, capture_output=True, text=True)
    
    # Check if execution was successful
    if execution_process.returncode != 0:
        print("Execution failed:")
        print(execution_process.stderr)
        return
    
    # Return the output of the program
    return execution_process.stdout

def convert_to_file(code_string, filename='code'):
    # Determine the file extension based on the code content
    file_extension = '.py'
    fe=0
    cpp_keywords = ['namespace', 'iostream', 'cin', 'cout']
    for keyword in cpp_keywords:
        if keyword in code_string:
            file_extension = '.cpp'
            fe=1
            
    c_keywords = ['stdio.h', 'stdlib.h', 'printf', 'scanf']
    for keyword in c_keywords:
        if keyword in code_string:
            file_extension = '.c'
            fe=2
            
    with open(filename + file_extension, 'w') as code_file:
        code_file.write(code_string)
        
    return fe

def tc_checker(l,l1,l2):
    fe=convert_to_file(l, filename='code')
    passed=0
    for x in range(len(l1)):
        if(fe==0):
            out=run_python_with_input('code.py',l1[x])
        if(fe==1):
            out=run_cpp_with_input('code.cpp',l1[x])
        else:
            out=run_c_with_input('code.c',l1[x])
        if(out.strip()==l2[x]):
            passed=passed+1
    return ("{} out of {} test cases passed".format(passed, len(l1)))