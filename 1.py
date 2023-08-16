import tkinter as tk                            #For GUI
from PIL import ImageTk							#For Images 
from tkinter import  messagebox					#For Info Box GUI
import mysql.connector as sql					#For Connecting DataBase With Project
import face_recognition							#For Recognizing Face 
import cv2										#For AI for face 
from openpyxl import Workbook					#For Marking Attndence In Excel
import datetime									#For Marking Date In Attendence Sheet
from tkinter import filedialog					#For Browsing Files 
import time as tm 								#For Displaying Time in Login Form
import shutil									#For Making A Copy Of Image In Folder
import os 									 	#For Deleting Image 


#Linking database 
mycon = sql.connect(host = 'localhost',
	user = 'root',
	passwd = '0000'
	,database = 'loginid')	

cursor = mycon.cursor()

#_____________Login Function___________():
def Login_Func() :
	a=Username_Entry.get()
	b=Password_Entry.get()

#_____________Verfiying Wether The Entry are not null___
	if a =='' and b=='':
		tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")

	elif a =='' :
		tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name")
	elif b =='' :
		messagebox.showinfo("Empty Or No Info", "Please Enter Password")
	elif a =='' and b=='':
		messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")
	elif a!='' and b!='':
		data = cursor.execute('select * from userid')
		data2 = cursor.fetchall()
		flag = 0
		#__________________Admin Dashboard____________________________
		for row in data2 :
			if row[0] ==a and row[1] ==b:
				print('Login Successfully')
				flag=1
				admindash()
							
		if flag == 0:
			messagebox.showerror("No Match", "Please Enter Correct Combination")

def clear() :
	Username_Entry.delete(0, 'end')	
	Password_Entry.delete(0, 'end')

def admindash() :
	Main.withdraw()	
	admin = tk.Toplevel()
	admin.geometry('1024x550+250+100')
	admin.resizable(False,False)
	admin.configure(bg='#ffffff')
	Admin_Frame =tk.LabelFrame(admin,font=('Verdana',18,'bold','italic'),
		fg='black',
		borderwidth=10,bg='#F2F2F5',padx=10,pady=5)
	Admin_Frame.pack(fill='x')
	
	Heading = tk.Label(Admin_Frame ,
		text = "Admin Dashboard \n Face Recognition Bassed Attendence ",
		font= ('Helvetica',19,'bold','italic'),
		bg='#F2F2F5',fg='Black',bd=10).pack(fill='x')
	
	Frame_Buttons = tk.LabelFrame(admin,text=' Features ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	Frame_Buttons.pack(anchor='w',padx=40,pady=6,fill='y')

	a=Username_Entry.get()
	b="Welcome "+a.capitalize()
	Add_label = tk.Label(admin,text=b ,bg='#ffffff',font=('helvatica',18,'bold'),fg='#67D8DA').place(x=400,y=125)

	#                         Addding Buttons 

	def add_student() :
		student_add = tk.Toplevel()
		student_add.geometry('545x311+470+240')
		Heading_Frame =tk.LabelFrame(student_add,font=('Verdana',18,'bold','italic'),
				fg='black',
				borderwidth=10,bg='#F2F2F5',padx=10,pady=5)
		Heading_Frame.pack(fill='x')
		heading = tk.Label(Heading_Frame,text='Add Details To System',font=('Helvetica',25),fg='#8A3C52').pack()
		Main_Frame_add = tk.LabelFrame(student_add,font=('Verdana',18,'bold','italic'),
				fg='black',
				borderwidth=10,bg='#F2F2F5',padx=10,pady=5)
		Main_Frame_add.pack(fill='x')
	

	
		global Name_label
		Name_label = tk.Label(Main_Frame_add,text='Please Enter Name :-',font=('helvatica',15,'bold'))
		Name_label.grid(row=0,column=1,padx =9,sticky='s')
		Name_Entry_add = tk.Entry(Main_Frame_add,width=25,bd=5,font=('helvatica',10,'bold'),fg='green')	
		Name_Entry_add.grid(row=1,column=1,padx =9)
		Name_Entry_add.focus_set()
		Identification_Id_entry =tk.Label(Main_Frame_add,text='Please Enter An Id :-',font=('helvatica',15,'bold'))
		Identification_Id_entry.grid(pady=5,row=2,column=1)
		global id_Entry_add
		id_Entry_add = tk.Entry(Main_Frame_add,width=25,bd=5,font=('helvatica',10,'bold'),fg='red')	
		id_Entry_add.grid(row=3,column=1,pady=5,padx =9)

		def add_file():
			global student_add_filename
			student_add_filename = filedialog.askopenfilename(initialdir='C:/',title='Select Picture',filetypes=(('JPG Files','*.jpg')
				,("All Files","*.*")))
		# Elements of Main_frame_add
		
		Button_Image = tk.Button(Main_Frame_add,command=add_file,text='Add\nImage',font=('Helvetica',15,'bold')
			,height=4,width=12,bd=5)
		Button_Image.grid(row=0,column=0,rowspan=2)

		def Submit():
			id_number = id_Entry_add.get()
			destination = "D:/Class 12/Computer Science/Group Project/face_data_img/"+id_number+".jpg"
			shutil.copy(student_add_filename,destination)
			print('Added Successfully')
			status_add = tk.Button(Main_Frame_add,height=5,text='Added',bg='green',state=tk.DISABLED,
				font=('helvatica',20,'bold')).grid(rowspan=4,column=2,row=0)
		
		button_Submit =tk.Button(Main_Frame_add,text='Submit',bg='Lightblue',font=('helvatica',10,'bold')
			,bd=5,width=15,command=Submit)
		button_Submit.grid(pady=5,row=2,column=0)
		global status_add
		status_add = tk.Button(Main_Frame_add,height=5,text='Status',bg='Red',state=tk.DISABLED
			,font=('helvatica',20,'bold')).grid(rowspan=4,column=2,row=0)


		def clear_add_data ():
			Name_Entry_add.delete(0, 'end')
			id_Entry_add.delete(0, 'end')
			status_add = tk.Button(Main_Frame_add,height=5,text='Status',bg='Red',state=tk.DISABLED
				,font=('helvatica',20,'bold')).grid(rowspan=4,column=2,row=0)

		button_Clear =tk.Button(Main_Frame_add,width=15,text='Clear',command=clear_add_data,bg='Pink'
			,font=('helvatica',10,'bold'),bd=5)
		button_Clear.grid(row=3,column=0,pady=5)


	
		


		student_add.mainloop()	



	Add_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/add.png')
	Add_Button = tk.Button(Frame_Buttons,text='Add Students',command=add_student,
		image=Add_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Add_label = tk.Label(Frame_Buttons,text="Add Data",bg='#ffffff',font=('helvatica',12,'bold')).pack()
	



	def delete_student() :
		delete_window = tk.Toplevel()
		delete_window.geometry('545x311+470+240')
		delete_window.config(bg='#FB7500')
		label_Heading = tk.Label(delete_window,text='Enter Info To Delete'
			,font=('Helvetica',16,"italic")).pack(anchor='center',side='top',fill='x')
		Frame_Body  = tk.LabelFrame(delete_window,text='Enter Details',font=('Helvetica',16,"italic")
			,borderwidth=8,bg='#FB7500',padx=10,pady=5)
		Frame_Body.pack(fill='x',pady=15)
		id_label = tk.Label(Frame_Body,text='Enter The Id Number Below',bg='#FB7500'
			,font=('Helvetica',16,"italic")).grid(row=0,column=0)
		global id_entry
		id_entry = tk.Entry(Frame_Body,width=15,bd=3,font=('Verdana',14,'bold','italic'),fg='Purple')
		id_entry.grid(row=0,column=1,padx=4)
		pass_label = tk.Label(Frame_Body,text='Enter The Current Password',bg='#FB7500'
			,font=('Helvetica',16,"italic")).grid(row=1,column=0)
		pass_entry = tk.Entry(Frame_Body,width=15,bd=3,font=('Verdana',14,'bold','italic'),fg='Purple')
		pass_entry.grid(row=1,column=1,padx=4,pady=7)
		status_new = tk.Label(delete_window,text='STATUS',bd=5,width=13,bg='BLUE',fg='black',font=('twencenta',14,'bold','italic'))
		status_new.pack(side='bottom',fill='x')






		def clear_delete_student(a=id_entry,b=pass_entry) :
			a.delete(0, 'end')	
			
			b.delete(0, 'end')

		def Submint_delete_student(direct='D:/Class 12/Computer Science/Group Project/face_data_img/'):
			z=Password_Entry.get()
			print(z)
			if pass_entry.get() == z :

				a = id_entry.get()
				delete  = direct+a+".jpg"
				os.remove(delete)
				status_new = tk.Label(delete_window,text='Successfully Deleted',bd=5,width=13,bg='Green'
					,fg='black',font=('twencenta',14,'bold','italic'))
				status_new.pack(side='bottom',fill='x')	

			else :
				s = tk.messagebox.showinfo('Error','Please Check Every Thing Its Coreect Or Not')
			
		Submint_button= tk.Button(Frame_Body,command=Submint_delete_student,text='Delete',bd=5,width=13,bg='pink'
			,fg='black',font=('twencenta',14,'bold','italic')).grid(row=2,column=1,padx=4,pady=7)

		clear_button= tk.Button(Frame_Body,command=clear_delete_student,text='Clear',bd=5,width=13,bg='Lightblue'
			,fg='black',font=('twencenta',14,'bold','italic')).grid(row=2,column=0,padx=4,pady=7)



	Remove_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/remove.png')
	Remove_Button = tk.Button(Frame_Buttons,image=Remove_img,borderwidth=0,bg='#ffffff',command=delete_student).pack()
	Remove_label = tk.Label(Frame_Buttons,text="Remove Data",bg='#ffffff',font=('helvatica',12,'bold')).pack()




	def attendence() :



		# Get a reference to webcam #0 (the default one)
		video_capture = cv2.VideoCapture(0)
			
			
		# Create a woorksheet
		book=Workbook()
		sheet=book.active

		known_face_encodings = []
		known_face_names = []	

		

		path, dirs, files = next(os.walk("D:/Class 12/Computer Science/Group Project/face_data_img"))
		file_count = len(files)    #number of images in folder
		

		for a in (1,file_count) :
			datalocation = 'D:/Class 12/Computer Science/Group Project/face_data_img/'+str(a)+".jpg"
			image_1 = face_recognition.load_image_file(datalocation)
			image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
			known_face_encodings.append(image_1_face_encoding)
			known_face_names.append(str(a))

		
			
		# Initialize some variables
		face_locations = []
		face_encodings = []
		face_names = []
		process_this_frame = True
			
		# Load present date and time
		now= datetime.datetime.now()
		today=now.day          #In formate of Numbers
		month=now.month        #In formate of Numbers
			
		   
		while True:
		 # Grab a single frame of video
			ret, frame = video_capture.read()
			
			# Resize frame of video to 1/4 size for faster face recognition processing
			small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
			
			# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
			rgb_small_frame = small_frame[:, :, ::-1]
			
			# Only process every other frame of video to save time
			if process_this_frame:
				# Find all the faces and face encodings in the current frame of video
				face_locations = face_recognition.face_locations(rgb_small_frame)
				face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

			
			face_names = []
			for face_encoding in face_encodings:
				# See if the face is a match for the known face(s)
				matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
				name = "Unknown"
			
				 # If a match was found in known_face_encodings, just use the first one.
				if True in matches:
					first_match_index = matches.index(True)
					name = known_face_names[first_match_index]
					# Assign attendance
					if int(name) in range(1,61):
						sheet.cell(row=int(name), column=int(today)).value = "Present"
					else:
						pass
			
				face_names.append(name)
			
			process_this_frame = not process_this_frame
			
			
			# Display the results
			for (top, right, bottom, left), name in zip(face_locations, face_names):
				   # Scale back up face locations since the frame we detected in was scaled to 1/4 size
				   top *= 4
				   right *= 4
				   bottom *= 4
				   left *= 4
			
			# Draw a box around the face
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			
			# Draw a label with a name below the face
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
			
			# Display the resulting image
			cv2.imshow('Video', frame)
				
			# Save Woorksheet as present month
			book.save(str(month)+'.xlsx')
			
			# Hit 'q' on the keyboard to quit!
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			
		# Release handle to the webcam
		video_capture.release()
		cv2.destroyAllWindows()







	Attendence_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Attendence.png')
	Attendence_Button = tk.Button(Frame_Buttons,image=Attendence_img,borderwidth=0,bg='#ffffff',command=attendence).pack()
	Attendence_label = tk.Label(Frame_Buttons,text="Attendence",bg='#ffffff',font=('helvatica',12,'bold')).pack()

	User_Frame = tk.LabelFrame(admin,text=' Accounts ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	User_Frame.place(x=830,y=120,)

	#                         Addding Buttons 

	def register_entry():
		global Username_entry
		global Password_Entry
		Userid = Username_entry.get()
		password = password_entry.get()
		cursor.execute("INSERT INTO userid (userid, pass)values('{}','{}')".format(Userid,password))
		mycon.commit()
		print('Registered Successfully')
	def registor_close(ESC):
		registorwindow.destroy()

	def registor():
		registorwindow = tk.Toplevel()
		registorwindow.title('Register')
		registorwindow.config(bg='lightblue')
		registorwindow.geometry('300x400+600+240')
		registorwindow.resizable('false','false')
		image =ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/register.png')
		registorimage=tk.Label(registorwindow,bg='lightblue',image=image)
		global Username_entry
		global password_entry
		global Name_entry
		Name=tk.Label(registorwindow,text='Enter Your Name :-',font=('twencenta',14,'bold','italic'),bg='lightblue')
		Name_entry=tk.Entry(registorwindow,width=35,bd=5)
		username=tk.Label(registorwindow,text='Enter UserName :-',font=('twencenta',14,'bold','italic'),bg='lightblue')
		Username_entry=tk.Entry(registorwindow,width=35,bd=5)
		password=tk.Label(registorwindow,text='Enter Password :-',font=('twencenta',14,'bold','italic'),bg='lightblue')
		password_entry=tk.Entry(registorwindow,width=35,bd=5)
		register_button= tk.Button(registorwindow,text='Register',bd=5,width=13,bg='pink',fg='black'
			,font=('twencenta',14,'bold','italic'),command=register_entry)
		clear_button= tk.Button(registorwindow,text='Clear',fg='white',width=13,bd=5,command=clear,bg='red'
			,font=('twencenta',14,'bold','italic'))
		register_button.grid(row=7,column=0,sticky='',pady=15)
		clear_button.grid(row=8,column=0,sticky='',pady=10)
		password.grid(row=5,column=0,sticky='',pady=5)
		password_entry.grid(row=6,column=0,sticky='')
		username.grid(row=3,column=0,sticky='',pady=5)
		Username_entry.grid(row=4,column=0,sticky='')
		Name.grid(row=1,column=0,sticky='',pady=5)
		Name_entry.grid(row=2,column=0,sticky='')
		registorimage.grid(row=0,column=0,sticky='ne')
		Name_entry.focus_set()
		print('Register Window Opened Successfully')
		registorwindow.mainloop()
		registorwindow.bind('<ESC>',registor_close)

	Autenticate_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Authenticate.png')
	Autenticate_Button = tk.Button(User_Frame,text='Add Students',command=registor
		,image=Autenticate_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Autenticate_label = tk.Label(User_Frame,text="Add User",bg='#ffffff',font=('helvatica',12,'bold')).pack()

	def change() :
		
		change_window = tk.Toplevel()
		change_window.geometry('545x311+470+240')
		change_window.config(bg='#FB7500')
		label_Heading = tk.Label(change_window,text='Change Password'
			,font=('Helvetica',16,"italic")).pack(anchor='center',side='top',fill='x')

		Frame_Heading = tk.LabelFrame(change_window,text='Enter Details',font=('Helvetica',16,"italic")
			,fg='black',borderwidth=8,bg='#FB7500',padx=10,pady=5)
		Frame_Heading.pack(fill='x',pady=15)

		username=tk.Label(Frame_Heading,text= 'UserName :-',font=('twencenta',14,'bold','italic'),bg='#FB7500')
		username_entry=tk.Entry(Frame_Heading,width=35,bd=5)
		username_entry.focus_set()
		old_password=tk.Label(Frame_Heading,text='Enter Old Password :-',font=('twencenta',14,'bold','italic'),bg='#FB7500')
		old_password_entry=tk.Entry(Frame_Heading,width=35,bd=5)
		new_password=tk.Label(Frame_Heading,text='Enter New Password :-',font=('twencenta',14,'bold','italic'),bg='#FB7500')
		new_password_entry=tk.Entry(Frame_Heading,width=35,bd=5)

		def update():
			a = username_entry.get()
			b = old_password_entry.get()
			c = new_password_entry.get()
			if a =='' and b=='' or c=='':
				tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")

			elif a =='' :
				tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name")
			elif b =='' :
				messagebox.showinfo("Empty Or No Info", "Please Enter Old Password")
			elif a =='' and b=='':
				messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")
			elif a!='' and b!='':
				data = cursor.execute('select * from userid')
				data2 = cursor.fetchall()
				flag = 0
				
				#__________________Admin Dashboard____________________________
				for row in data2 :
					if row[0] ==a and row[1] ==b:
						dataxyz="UPDATE userid SET pass='{}' WHERE userid='{}';".format(c,a)
						cursor.execute(dataxyz)
						mycon.commit()
						flag = 1
						status.destroy()
						global status_new
						status_new = tk.Label(change_window,text='Successfully Changed',bd=5,width=13,bg='Green'
							,fg='black',font=('twencenta',14,'bold','italic'))
						status_new.pack(side='bottom',fill='x')		
				if flag == 0:
					messagebox.showerror("No Match", "Please Enter Correct Combination")
		update_button= tk.Button(Frame_Heading,text='Update',command=update,bd=5,width=13,bg='pink',fg='black'
			,font=('twencenta',14,'bold','italic'))
		def clear_1():
			username_entry.delete(0, 'end')	
			
			old_password_entry.delete(0, 'end')

			new_password_entry.delete(0, 'end')

			

		clear_button= tk.Button(Frame_Heading,command=clear_1,text='Clear',bd=5,width=13,bg='Lightblue',fg='black'
			,font=('twencenta',14,'bold','italic'))
		global status
		status = tk.Label(change_window,text='Status',bd=5,width=13,bg='pink',fg='black',font=('twencenta',14,'bold','italic'))
		#alingment
		username.grid(row=0,column=0,pady=2)
		username_entry.grid(row=0,column=1,pady=2)
		old_password.grid(row=1,column=0,pady=2)
		old_password_entry.grid(row=1,column=1,pady=2)
		new_password.grid(row=2,column=0,pady=2)
		new_password_entry.grid(row=2,column=1,pady=2)
		update_button.grid(row=3,column=1,pady=2)
		clear_button.grid(sticky='e',row=3,column=0,pady=2,padx=4)
		status.pack(side='bottom',fill='x')

		change_window.mainloop() 

	Change_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Password_Change.png')
	Change_Button = tk.Button(User_Frame,image=Change_img,command=change,borderwidth=0,bg='#ffffff').pack()
	Change_label = tk.Label(User_Frame,text="Change Password",bg='#ffffff',font=('helvatica',12,'bold')).pack()



	def log_out():
		admin.destroy()
		Main.deiconify()

	Logout_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Logout_img.png')
	Logout_Button = tk.Button(User_Frame,image=Logout_img,borderwidth=0,bg='#ffffff',command=log_out).pack()
	Attendence_label = tk.Label(User_Frame,text="Logout",bg='#ffffff',font=('Cantarell',12,'bold')).pack(fill='x')

	info_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/in.gif')
	info_dev = tk.Button(admin,image = info_img,bg='#ffffff',command=dev_info,borderwidth=1,bd=0).place(x=480,y=425)
	admin.mainloop()
   
#____________________________________________________________________________________________________________________________


#_______Login Window____________
Main = tk.Tk()
Main.title('Face Recognition Bassed Attendence Software')
Main.geometry('1024x550+250+100')
Main.resizable(False,False)

#_______Background_______________
Bgimage = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/bg.jpg') 
bgimage = tk.Label(Main,image=Bgimage,borderwidth=0).place(x=0,y=0,)
#_______Images____________________
login_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Login.png')
reset_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/Reset1.png')

#_______Labels___________________

frame_1 = tk.LabelFrame(Main,text=' Login Section ',font=('Verdana',18,'bold','italic'),fg='black',borderwidth=10
	,bg='#FEEDD1',padx=50,pady=30)
frame_1.place(x=250,y=150)

Username_Label = tk.Label(frame_1,text='Username :-',bd=5,font=('Verdana',17,'bold','italic'),bg='#FEEDD1',fg='Black')
Username_Label.grid(row=0,column=0,pady=5)
Username_Entry = tk.Entry(frame_1,width=15,bd=5,font=('Verdana',14,'bold','italic'),fg='Purple')
Username_Entry.grid(row=0,column=2,padx=5)
Password_Label = tk.Label(frame_1,text='Password :-',font=('Verdana',17,'bold','italic'),bg='#FEEDD1',fg='Black')
Password_Label.grid(row=3,column=0,pady=5)
global Password_Entry
Password_Entry = tk.Entry(frame_1,width=15,bd=5,show='*',font=('Verdana',14,'bold','italic'),fg='Purple')
Password_Entry.grid(row=3,column=2,padx=5)
Login_Button = tk.Button(frame_1,image=login_img,font=('Helvatica',14,'bold','italic'),bg='#FEEDD1',command=Login_Func,borderwidth=0)
Login_Button.grid(row=4,column=2,pady=20,sticky='e')
Reset_Button = tk.Button(frame_1,image=reset_img,font=('Helvatica',14,'bold','italic'),bd=0,command=clear,bg='#FEEDD1',)
Reset_Button.grid(row=4,column=0,pady=20,sticky='w')

def dev_info():
	Info = tk.messagebox.showinfo(title="Developers Info", message='Developed By\n1.Shri Ganesh Purohi')

info_img = ImageTk.PhotoImage(file ='D:/Class 12/Computer Science/Group Project/Assets/in.gif')
info_dev = tk.Button(Main,image = info_img,bg='#DDBEA2',command=dev_info,borderwidth=1,bd=0).place(x=480,y=475)



def clock():
	hour = tm.strftime('%I')
	minute = tm.strftime('%M')
	second = tm.strftime('%S')
	am_pm = tm.strftime('%p')
	date = tm.strftime('%d')
	month = tm.strftime('%b')
	year = tm.strftime('%Y')
	Time_Label.config(text=date+"-"+month+"-"+year+"  "+ hour +":"+ minute +":"+second+':'+am_pm)
	Time_Label.after(1000,clock)
def update():
	Time_Label.config(text='New Time')
	
Time_Label = tk.Label(frame_1,text=" ",font=('Helvatica',14,'bold','italic'),bg='#FEEDD1',fg='blue',highlightbackground="black")
Time_Label.grid(row=5,columnspan=3)

Time_Label.after(5000,update)
clock()


#____Set Focus On User Name ______

Username_Entry.focus_set()

Main.mainloop()
