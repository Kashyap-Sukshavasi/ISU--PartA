import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_volume():
    shape = shape_var.get()
    volume = 0

    if shape == "Cube":
        try:
            edge_length = float(edge_length_entry.get())
            volume = edge_length ** 3
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Cube")
    elif shape == "Cylinder":
        try:
            radius = float(cylinder_radius_entry.get())
            height = float(cylinder_height_entry.get())
            volume = 3.14159265359 * (radius ** 2) * height
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Cylinder")
    elif shape == "Pyramid":
        try:
            base_length = float(pyramid_base_length_entry.get())
            height = float(pyramid_height_entry.get())
            volume = (1 / 3) * (base_length ** 2) * height
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Pyramid")
    elif shape == "Cone":
        try:
            radius = float(cone_radius_entry.get())
            height = float(cone_height_entry.get())
            volume = (1 / 3) * 3.14159265359 * (radius ** 2) * height
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Cone")

    selected_unit = unit_var.get()
    unit_str = selected_unit + "³"

    messagebox.showinfo(f"Volume of {shape}", f"Volume of {shape}: {volume:.2f} {unit_str}")

def update_layout():
    shape = shape_var.get()

    if shape == "Cube":
        edge_length_label.grid(row=2, column=0)
        edge_length_entry.grid(row=2, column=1)
        edge_length_unit.grid(row=2, column=2)
        cylinder_radius_label.grid_forget()
        cylinder_radius_entry.grid_forget()
        cylinder_radius_unit.grid_forget()
        cylinder_height_label.grid_forget()
        cylinder_height_entry.grid_forget()
        cylinder_height_unit.grid_forget()
        pyramid_base_length_label.grid_forget()
        pyramid_base_length_entry.grid_forget()
        pyramid_base_length_unit.grid_forget()
        pyramid_height_label.grid_forget()
        pyramid_height_entry.grid_forget()
        pyramid_height_unit.grid_forget()
        cone_radius_label.grid_forget()
        cone_radius_entry.grid_forget()
        cone_radius_unit.grid_forget()
        cone_height_label.grid_forget()
        cone_height_entry.grid_forget()
        cone_height_unit.grid_forget()
    elif shape == "Cylinder":
        edge_length_label.grid_forget()
        edge_length_entry.grid_forget()
        edge_length_unit.grid_forget()
        cylinder_radius_label.grid(row=2, column=0)
        cylinder_radius_entry.grid(row=2, column=1)
        cylinder_radius_unit.grid(row=2, column=2)
        cylinder_height_label.grid(row=3, column=0)
        cylinder_height_entry.grid(row=3, column=1)
        cylinder_height_unit.grid(row=3, column=2)
        pyramid_base_length_label.grid_forget()
        pyramid_base_length_entry.grid_forget()
        pyramid_base_length_unit.grid_forget()
        pyramid_height_label.grid_forget()
        pyramid_height_entry.grid_forget()
        pyramid_height_unit.grid_forget()
        cone_radius_label.grid_forget()
        cone_radius_entry.grid_forget()
        cone_radius_unit.grid_forget()
        cone_height_label.grid_forget()
        cone_height_entry.grid_forget()
        cone_height_unit.grid_forget()
    elif shape == "Pyramid":
        edge_length_label.grid_forget()
        edge_length_entry.grid_forget()
        edge_length_unit.grid_forget()
        cylinder_radius_label.grid_forget()
        cylinder_radius_entry.grid_forget()
        cylinder_radius_unit.grid_forget()
        cylinder_height_label.grid_forget()
        cylinder_height_entry.grid_forget()
        cylinder_height_unit.grid_forget()
        pyramid_base_length_label.grid(row=2, column=0)
        pyramid_base_length_entry.grid(row=2, column=1)
        pyramid_base_length_unit.grid(row=2, column=2)
        pyramid_height_label.grid(row=3, column=0)
        pyramid_height_entry.grid(row=3, column=1)
        pyramid_height_unit.grid(row=3, column=2)
        cone_radius_label.grid_forget()
        cone_radius_entry.grid_forget()
        cone_radius_unit.grid_forget()
        cone_height_label.grid_forget()
        cone_height_entry.grid_forget()
        cone_height_unit.grid_forget()
    elif shape == "Cone":
        edge_length_label.grid_forget()
        edge_length_entry.grid_forget()
        edge_length_unit.grid_forget()
        cylinder_radius_label.grid_forget()
        cylinder_radius_entry.grid_forget()
        cylinder_radius_unit.grid_forget()
        cylinder_height_label.grid_forget()
        cylinder_height_entry.grid_forget()
        cylinder_height_unit.grid_forget()
        pyramid_base_length_label.grid_forget()
        pyramid_base_length_entry.grid_forget()
        pyramid_base_length_unit.grid_forget()
        pyramid_height_label.grid_forget()
        pyramid_height_entry.grid_forget()
        pyramid_height_unit.grid_forget()
        cone_radius_label.grid(row=2, column=0)
        cone_radius_entry.grid(row=2, column=1)
        cone_radius_unit.grid(row=2, column=2)
        cone_height_label.grid(row=3, column=0)
        cone_height_entry.grid(row=3, column=1)
        cone_height_unit.grid(row=3, column=2)

app = tk.Tk()
app.title("Shape Volume Calculator")

# Create variables for the shape choice and the input fields
shape_var = tk.StringVar()
shape_var.set("Cube")

unit_var = tk.StringVar()
unit_var.set("Meters")

# Shape choice radio buttons
shape_label = tk.Label(app, text="Select a Shape:")
shape_label.grid(row=0, column=0)

cube_radio = tk.Radiobutton(app, text="Cube", variable=shape_var, value="Cube", command=update_layout)
cube_radio.grid(row=1, column=0)

cylinder_radio = tk.Radiobutton(app, text="Cylinder", variable=shape_var, value="Cylinder", command=update_layout)
cylinder_radio.grid(row=1, column=1)

pyramid_radio = tk.Radiobutton(app, text="Pyramid", variable=shape_var, value="Pyramid", command=update_layout)
pyramid_radio.grid(row=1, column=2)

cone_radio = tk.Radiobutton(app, text="Cone", variable=shape_var, value="Cone", command=update_layout)
cone_radio.grid(row=1, column=3)

# Input fields for different shapes
edge_length_label = tk.Label(app, text="Enter the edge length:")
edge_length_entry = tk.Entry(app)
edge_length_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
edge_length_unit.grid(row=2, column=2)
edge_length_unit.set("Meters")

cylinder_radius_label = tk.Label(app, text="Enter the radius:")
cylinder_radius_entry = tk.Entry(app)
cylinder_radius_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
cylinder_radius_unit.grid(row=2, column=2)
cylinder_radius_unit.set("Meters")

cylinder_height_label = tk.Label(app, text="Enter the height:")
cylinder_height_entry = tk.Entry(app)
cylinder_height_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
cylinder_height_unit.grid(row=3, column=2)
cylinder_height_unit.set("Meters")

pyramid_base_length_label = tk.Label(app, text="Enter the base length:")
pyramid_base_length_entry = tk.Entry(app)
pyramid_base_length_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
pyramid_base_length_unit.grid(row=2, column=2)
pyramid_base_length_unit.set("Meters")

pyramid_height_label = tk.Label(app, text="Enter the height:")
pyramid_height_entry = tk.Entry(app)
pyramid_height_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
pyramid_height_unit.grid(row=3, column=2)
pyramid_height_unit.set("Meters")

cone_radius_label = tk.Label(app, text="Enter the radius:")
cone_radius_entry = tk.Entry(app)
cone_radius_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
cone_radius_unit.grid(row=2, column=2)
cone_radius_unit.set("Meters")

cone_height_label = tk.Label(app, text="Enter the height:")
cone_height_entry = tk.Entry(app)
cone_height_unit = ttk.Combobox(app, values=["Meters", "Feet"], textvariable=unit_var)
cone_height_unit.grid(row=3, column=2)
cone_height_unit.set("Meters")

update_layout()  # Initialize the layout based on the default shape

# Calculate button
calculate_button = tk.Button(app, text="Calculate", command=calculate_volume)
calculate_button.grid(row=4, column=0, columnspan=2)

# Exit button
exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.grid(row=4, column=2, columnspan=2)

app.mainloop()
