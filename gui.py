import tkinter as tk
import subprocess

def run_bash_file(bash_file):
    try:
        subprocess.run(['bash', bash_file])
    except Exception as e:
        print(f"An error occurred: {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title('Conda Environment Runner')

# Instructions Textbox
instructions = tk.Text(root, height=10, width=100)
instructions.pack()
instructions.insert(tk.END, "Instructions:\n")
instructions.insert(tk.END, "1. Copy the input files in the folder 'dicomsample'.\n\n")
instructions.insert(tk.END, "2. The output of predictions is in the text file 'results_dicomsample.csv'.\n\n")
instructions.insert(tk.END, "3. The output of segmentations is in the folder 'segment'.\n\n")

# Button for Predict
predict_button = tk.Button(root, text='Predict', command=lambda: run_bash_file('run_predict.sh'),
                           height=10, width=30, bg='blue', fg='white')
predict_button.pack()

# Button for Segmentation
segmentation_button = tk.Button(root, text='Segmentation', command=lambda: run_bash_file('segmentation.sh'),
                                height=10, width=30, bg='green', fg='white')
segmentation_button.pack()

# Button for Common 2D Measurements
common_2D_measurements_button = tk.Button(root, text='Common 2D Measurements', command=lambda: run_bash_file('common_2D_measurements.sh'),
                                          height=10, width=30, bg='yellow', fg='black')
common_2D_measurements_button.pack()

# Button for Global Longitudinal Strain
global_longitudinal_strain_button = tk.Button(root, text='Global Longitudinal Strain', command=lambda: run_bash_file('global_longitudinal_strain.sh'),
                                              height=10, width=30, bg='red', fg='white')
global_longitudinal_strain_button.pack()

# Start the Tkinter event loop
root.mainloop()

