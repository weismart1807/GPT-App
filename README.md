# GPT_API
### First, you need to prepare a OpenAI GPT API, then using GPT API creats application.

# gpt chat with each other
### Let two GPT roles discuss a topic you choose and eventually reach the same conclusion.
Steps:
1. Replace the GPT API key with your own.
2. Open your terminal and run: python app.py
3. Open your browser and go to: http://127.0.0.1:5000
4. You should see a page like this:
![image](https://github.com/user-attachments/assets/9ffdb6dd-77a9-49ae-93e5-52fe0f861e73)

# gpt from video
### Generate a summary and extract key topics from a URL you provide.
Steps:
1. Replace the GPT API key with your own.
2. In the terminal, run: npm run dev
3. Open your browser and go to: http://localhost:3001
4. You should see a page like this:
![image](https://github.com/user-attachments/assets/1fcde996-a09f-4c31-b829-d48b8d4b77e6)


# gpt2
### Generate a summary and identify key topics from an article you provide.
Steps:
1. Replace the GPT API key with your own.
2. In the terminal, run: node server.js
3. Open your browser and go to: http://localhost:3002
4. You should see a page like this:
![image](https://github.com/user-attachments/assets/b5aa2390-7757-48e0-88ce-e52911ac1639)

# gptapi
### (API) Accepts an article and returns a summary along with key topics.
Steps:
1. Change GPT Key for yourself
2. Open text.json and change text for yourself
3. Go to terminal 1 and command " node server.cjs "
4. Go to terminal 2 and command " curl -X POST -H "Content-Type: application/json; charset=UTF-8" -d @text.json http://localhost:20080/api/generate "
5. You can see resposes in reponse file
6. Then, you can see the image below
<img width="569" alt="image" src="https://github.com/user-attachments/assets/4e392569-ce9a-408f-9af1-de178637c302">
