import tkinter as tk
from tkinter import ttk, filedialog
import os 
import shutil





def navTo_auto():
    mainframe.pack_forget()
    auto_frame.pack(fill='both', expand=True)



images = ['.jpeg','.jpg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.raw', '.eps', '.pdf', '.psd','.ico']
videos = [".mp4", ".avi", ".mov"]
audio = [".mp3",".aac",".wav"]
docs =  [".txt", ".md", ".py", ".html", ".css", ".js", ".json", ".xml", ".csv", ".log"]




def sort_files():
    fileType  = file_type.get()
    destination = dest_entry.get()
    if source_folder.get() == "":
        source_folder.configure(bg='red')
        return
    if destination == "":
        dest_entry.configure(bg="red")
        return
    os.chdir(source_folder.get())
    files = os.listdir()
    if fileType == "Pictures":
        for file in files:
            name,ext = os.path.splitext(file)
            if ext in images:
                shutil.move(file,destination)
                label_name.configure(text=f'The image files were moved from {source_folder.get()} to {destination}',font=('arial',10),bg='green',fg='black')

    if fileType == "Music":
        for file in files:
            name,ext = os.path.splitext(file)
            if ext in audio:
                shutil.move(file,destination)
                label_name.configure(text=f'The audio files were moved from {source_folder.get()} to {destination}',font=('arial',10),bg='green',fg='black')

    if fileType == "Videos":
        for file in files:
            name,ext = os.path.splitext(file)
            if ext in videos:
                shutil.move(file,destination)
                label_name.configure(text=f'The video files were moved from {source_folder.get()} to {destination}',font=('arial',10),bg='green',fg='black')
    if fileType == "Documents":
        for file in files:
            name,ext = os.path.splitext(file)
            if ext in docs:
                shutil.move(file,destination)
                label_name.configure(text=f'The video files were moved from {source_folder.get()} to {destination}',font=('arial',10),bg='green',fg='black')




def auto_sort():
    if source_folder_entry.get() == "":
        source_folder_entry.configure(bg='red')
        return
    if dest_folder_entry.get() == "":
        dest_folder_entry.configure(bg='red')
        return
    os.chdir(source_folder_entry.get())
    files = os.listdir()
    auto_dest = dest_folder_entry.get()
    pic_path = auto_dest + "/myPictures"
    music_path = auto_dest + "/myMusic"
    vid_path = auto_dest + "/myVideos"
    doc_path = auto_dest + "/myDocuments"
    
    try:
        os.mkdir(pic_path)
        os.mkdir(vid_path)
        os.mkdir(music_path)
        os.mkdir(doc_path)
        print("Folders  %s created!" % auto_dest)
    except FileExistsError:
        print("Folder %s already exists" % auto_dest)
        return
    
    for file in files:
        name,ext = os.path.splitext(file)
        if ext in images:
            shutil.move(file,pic_path)
        elif ext in videos:
            shutil.move(file,vid_path)
        elif ext in audio:
            shutil.move(file,music_path)
        elif ext in docs:
            shutil.move(file,doc_path)
    auto_status_label.configure(text=f"The files have been moved to their respective folders in {auto_dest}", font=("Arial", 6))


# Create the root window
root = tk.Tk()
root.title("Files organizer by jude")
root.geometry("800x800")
root.configure(bg="#000000")

# Create a frame inside the root window
mainframe = tk.Frame(root, bg="black")
mainframe.pack(padx=50, pady=20, fill='both', expand=True)

# Add a label to the frame
label_title = tk.Label(mainframe, text="Files organizer", font=("Arial", 30, "bold"), bg="#222222", fg="#FFFFFF")
label_title.pack(pady=(10, 10))

label_name = tk.Label(mainframe, text="Browse below for the files to move and \n select their source and destination folders\n If you have a large folder,press the auto button to quickly auto sort.", font=("Arial", 15), bg="black", fg="white",)
label_name.pack(fill='x', padx=10, pady=(0, 10),ipady=30)


# Add a dropdown options entry for the name
file_type_label = tk.Label(mainframe, text="Get these files:", font=("Arial", 15), bg="brown", fg="yellow")
file_type_label.pack(fill='x', padx=20, pady=(0, 10))
options = ['Pictures', 'Videos', 'Music', 'Documents']
file_type = ttk.Combobox(mainframe, values=options, font=("Arial", 16), state='readonly')
file_type.current(0)
file_type.pack(fill='x', padx=20, pady=(0, 20))

# Add an entry for the email address
source_folder_label = tk.Label(mainframe, text="From these folder:",font=("Arial", 15), bg="brown", fg="yellow")
source_folder_label.pack(fill='x', padx=20, pady=(0, 10))
source_folder = tk.Entry(mainframe, font=("Arial", 16), bg="#666666", fg="#FFFFFF")
source_folder.pack(fill='x', padx=20, pady=(0, 20))
def browse_email():
    path = filedialog.askdirectory(title="Select Email Directory")
    if path:
        source_folder.delete(0, 'end')
        source_folder.insert(0, path)
button_browse_email = tk.Button(mainframe, text="Browse", font=("Arial", 12), bg="tan", fg="black", command=browse_email)
button_browse_email.pack(pady=(0, 20))

# Add an entry for the phone number
dest_label = tk.Label(mainframe, text="And move to this folder:", font=("Arial", 15), bg="brown", fg="yellow")
dest_label.pack(fill='x', padx=20, pady=(0, 10))
dest_entry = tk.Entry(mainframe, font=("Arial", 16), bg="#666666", fg="#FFFFFF")
dest_entry.pack(fill='x', padx=20, pady=(0, 20))
def browse_phone():
    path = filedialog.askdirectory(title="Select Phone Directory")
    if path:
        dest_entry.delete(0, 'end')
        dest_entry.insert(0, path)
button_browse_phone = tk.Button(mainframe, text="Browse", font=("Arial", 12), bg="tan", fg="black", command=browse_phone)
button_browse_phone.pack(pady=(0, 20))

# Add a button to the frame
button_organize = tk.Button(mainframe, text="organize", font=("Arial", 13, "bold"), bg="green", fg="black",border=4,command=sort_files)
button_organize.place(y=570,x=310)

button_auto = tk.Button(mainframe, text="Auto mode", font=("Arial", 13, "bold"), bg="brown", fg="black",border=4,command=navTo_auto)
button_auto.place(y=575,x=520)

auto_frame = tk.Frame(root, bg="black")
#auto_frame.pack(fill="both", expand=True, padx=20, pady=20)

auto_text ="In auto mode,the programs creates a new folder with \n subfolders and moves the files from the selected folder below to theri respective new folder.\n The folder created has the following subfolders:Pictures,Music,Videos,Documents."

auto_inst_label = tk.Label(auto_frame, text=auto_text, font=("Arial", 12), fg="white", bg="black")
auto_inst_label.pack(pady=20, padx=20)

source_folder_label = tk.Label(auto_frame, text="Choose the folder with the files to be sorted", font=("Arial", 12), fg="white", bg="black")
source_folder_label.pack(pady=(50, 10))

def open_directory():
    folder_path = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, folder_path)

source_folder_entry = tk.Entry(auto_frame, font=("Arial", 14), width=30)
source_folder_entry.pack(pady=10)

source_folder_button = tk.Button(auto_frame, text="Browse", font=("Arial", 14), command=open_directory)
source_folder_button.pack(pady=10)

####
dest_folder_label = tk.Label(auto_frame, text="Choose where the sorted folder will be created at", font=("Arial", 12), fg="white", bg="black")
dest_folder_label.pack(pady=(50, 10))

def open_directory():
    folder_path = filedialog.askdirectory()
    dest_folder_entry.delete(0, tk.END)
    dest_folder_entry.insert(0, folder_path)

dest_folder_entry = tk.Entry(auto_frame, font=("Arial", 14), width=30)
dest_folder_entry.pack(pady=10)

dest_folder_button = tk.Button(auto_frame, text="Browse", font=("Arial", 14), command=open_directory)
dest_folder_button.pack(pady=10)
###

button_auto_sort = tk.Button(auto_frame, width=8, text="sort", font=("Arial", 13, "bold"), bg="brown", fg="black",border=4,command=auto_sort)
button_auto_sort.pack(pady=30)

auto_status_label = tk.Label(auto_frame, text='', font=("Arial", 12), fg="white", bg="black")
auto_status_label.pack(pady=20, padx=20)


# Run the main loop of the GUI
root.mainloop()
