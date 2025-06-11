from openai import OpenAI
import subprocess
gemini_api_key = "AIzaSyB9fHK2qUPekNQRd4jVZDUbxYWmK-xukqc"
model = OpenAI(api_key = gemini_api_key , base_url = "https://generativelanguage.googleapis.com/v1beta/openai/")
def my_model(prompt):
        mymsg = [
            {"role" : "system" , "content": "you have to act as a devops engineer and give commands to the user whatever they want to perform . just give the linux commands to the user no need of any other stuffs. the content should be like if the user is asking for the date right now then you should simple give them output as date ."},
            {"role" : "user" , "content" : prompt}
            ]
        output = model.chat.completions.create(
            messages = mymsg,
            model="gemini-2.0-flash"
        )
        return output.choices[0].message.content
instruction = input("enter your instruction: ")
result = my_model(instruction)
print('This is the command :'+result)
choice = input("want to proceed(Y/N): ")
if choice == "Y":
	display = subprocess.run("date", shell=True, capture_output=True, text=True)
	print("Your output is:", result.stdout.strip())
else :
	print("No command is runned")