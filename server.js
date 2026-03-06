const express=require("express")
const bodyParser=require("body-parser")
const {spawn}=require("child_process")

const app=express()

app.use(bodyParser.json())
app.use(express.static(__dirname))

app.post("/chat",(req,res)=>{

const question=req.body.message

const py=spawn("python",["gym_assistant.py"])

let output=""

py.stdout.on("data",(data)=>{
output+=data.toString()
})

py.stdin.write(question+"\n")
py.stdin.end()

py.on("close",()=>{
res.json({reply:output})
})

})

app.listen(3000,()=>{
console.log("Server running on http://localhost:3000")
})