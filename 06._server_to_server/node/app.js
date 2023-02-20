import express from "express";

const app = express()

app.get("/date", (req, res) => {
    res.send(new Date())
})

app.get("/datefromfastapi", async (req, res) => {
    const response = await fetch('http://127.0.0.1:8000/date');
    const body = await response.json();
    res.send(body)
})

const PORT = 8080

app.listen(PORT, () => console.log("Server is running on port", PORT))