# GPT_API
using GPT API creats application

# gpt chat with each other
1. change GPT Key for yourself
2. go to trminal and command "python app.py"
3. open your chrome and search http://127.0.0.1:5000
4. you can see the image below
![image](https://github.com/user-attachments/assets/9ffdb6dd-77a9-49ae-93e5-52fe0f861e73)

# gpt from video
1. change GPT Key for yourself
2. go to trminal and command "npm run dev"
3. open your chrome and search http://localhost:3001/
4. you can see the image below
![image](https://github.com/user-attachments/assets/1fcde996-a09f-4c31-b829-d48b8d4b77e6)


# gpt2
1. change GPT Key for yourself
2. go to trminal and command "node server.js"
3. open your chrome and search http://localhost:3002/
4. you can see the image below
![image](https://github.com/user-attachments/assets/b5aa2390-7757-48e0-88ce-e52911ac1639)

# gptapi
1. change GPT Key for yourself
2. go to terminal 1 and command "node server.js"
3. go to terminal 2 and command "Invoke-WebRequest -Uri "http://localhost:20080/api/generate" -Method POST -ContentType "application/json; charset=UTF-8" -Body '{"text": "..."}' -UseBasicParsing"
4. OR go to terminal 2 and command  
   $text = '...'  
   $jsonBody = @{ text = $text } | ConvertTo-Json  
   $response = Invoke-RestMethod -Uri "http://localhost:20080/api/generate" -Method POST -ContentType "application/json; charset=UTF-8" -Body $jsonBody   
   Write-Output $($response.summary)  
   Write-Output $($response.topics)
5. you can see resposesin reponse file
