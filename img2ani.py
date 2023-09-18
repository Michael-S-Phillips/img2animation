import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import imageio
import threading

# Create a class for the Image Animation App
class ImageAnimationApp:
    def __init__(self, root):
        # Initialize the root window and set its title
        self.root = root
        self.root.title("Image Animation")

        # Set default values for animation format and speed
        self.animation_format = tk.StringVar(value="mp4")  # Default value
        self.animation_speed = tk.DoubleVar(value=30)  # Default speed in frames per second

        # Initialize the preview status
        self.preview_running = False

        # Create buttons and UI elements
        self.load_images_button = tk.Button(self.root, text="Load Images", command=self.load_images)
        self.load_images_button.pack()

        self.format_menu = tk.OptionMenu(self.root, self.animation_format, "gif", "mp4")
        self.format_menu.pack()

        self.animation_speed_label = tk.Label(self.root, text="Animation Speed (fps):")
        self.animation_speed_label.pack()

        self.animation_speed_scale = tk.Scale(self.root, variable=self.animation_speed, from_=2, to=120, resolution=1, orient="horizontal")
        self.animation_speed_scale.pack()

        self.preview_button = tk.Button(self.root, text="Preview Animation", command=self.create_preview_window)
        self.preview_button.pack() 

        self.save_button = tk.Button(self.root, text="Save Animation", command=self.save_animation)
        self.save_button.pack()

    def image_generator(self):
        # Generator function that yields images one by one from the list of image paths
        for image_path in self.image_paths:
            yield Image.open(image_path)

    def load_images(self):
        # Open a file dialog to select multiple image files
        self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")])

        # Generate images using the image path generator
        self.images_generator = self.image_generator()

        # Print the number of images loaded
        print(f"Images loaded: {len(self.image_paths)}")

    def create_preview_window(self):
        # Create a separate preview window
        self.images_generator = self.image_generator()  # Reset the generator
        image = next(self.images_generator)  # Get the first image
        self.image_tk = ImageTk.PhotoImage(image)  # Convert the image to Tkinter-compatible format

        # Create the preview window
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Animation Preview")

        # Create a canvas for displaying the preview image
        preview_canvas = tk.Canvas(preview_window, width=self.image_tk.width(), height=self.image_tk.height())
        preview_canvas.pack()

        self.preview_label = tk.Label(preview_canvas)  # Label for displaying the image
        self.preview_label.pack()

        speed_frame = tk.Frame(preview_window)
        speed_frame.pack()

        speed_label = tk.Label(speed_frame, text="Animation Speed (fps):")
        speed_label.pack(side=tk.LEFT)

        speed_slider = tk.Scale(speed_frame, from_=2, to=100, resolution=1, orient=tk.HORIZONTAL, variable=self.animation_speed)
        speed_slider.pack(side=tk.LEFT)

        preview_controls = tk.Frame(preview_window)
        preview_controls.pack()

        # Buttons for controlling the preview
        play_button = tk.Button(preview_controls, text="Play", command=self.start_preview)
        play_button.pack(side=tk.LEFT)

        stop_button = tk.Button(preview_controls, text="Stop", command=self.stop_preview)
        stop_button.pack(side=tk.LEFT)
        
        restart_button = tk.Button(preview_controls, text="Restart", command=self.restart_preview)
        restart_button.pack(side=tk.LEFT)

    def play_preview(self):
        # Play the animation preview
        try:
            image = next(self.images_generator)  # Get the next image
            image_tk = ImageTk.PhotoImage(image)  # Convert the image to Tkinter-compatible format
            self.preview_label.config(image=image_tk)  # Update the image in the label
            self.preview_label.image = image_tk

            if self.preview_running:
                delay = int(1000 / self.animation_speed.get())  # Calculate the delay between frames
                self.root.after(delay, self.play_preview)  # Schedule the next frame to be displayed
        except StopIteration:
            # Preview reached the end, stop the animation
            self.preview_running = False

    def start_preview(self):
        # Start the animation preview loop
        self.preview_running = True
        self.play_preview()

    def stop_preview(self):
        # Stop the animation preview
        self.preview_running = False

    def restart_preview(self):
        # Restart the animation preview from the beginning
        self.images_generator = self.image_generator() # Reset the generator to the beginning
        self.start_preview()  # Start the preview again

    def save_animation(self):
        # Save the animation as either GIF or MP4 format
        if not self.images_generator:
            return

        output_format = self.animation_format.get()

        if output_format == "gif":
            # Save as GIF format
            output_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
            try:
                with imageio.get_writer(output_path, mode="I", duration=1000/self.animation_speed.get()) as writer:
                    for image in self.image_generator():
                        writer.append_data(image)
            except Exception as e:
                print("Error saving GIF: ",e)

        elif output_format == "mp4":
            # Save as MP4 format
            output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
            self.save_mp4(output_path)

        # Print the output path after saving
        print(f"Animation saved as: {output_path}")

    def save_mp4(self, output_path):
        # Save the animation as MP4 format using a separate thread
        def write_frames():
            with imageio.get_writer(output_path, fps=self.animation_speed.get()) as writer:
                for image in self.image_generator():
                    image = np.array(image)  
                    writer.append_data(image)
        
        threading.Thread(target=write_frames).start()

def main():
    # Create the main Tkinter window and the ImageAnimationApp instance
    root = tk.Tk()
    app = ImageAnimationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
