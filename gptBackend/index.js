const express = require('express');
const axios = require('axios');
const cors = require("cors");
require("dotenv").config();
const { Configuration, OpenAIApi } = require("openai");

const app = express();
const port = process.env.mongoPort;

app.use(express.json());
app.use(cors());
const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
  const openai = new OpenAIApi(configuration);

// API endpoint to receive user messages
app.post('/chat', async (req, res) => {
  const userMessage = req.body.message;

  try {
    // Send user message to ChatGPT API


    const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: userMessage,
        temperature: 1,
        max_tokens: 256,
        top_p: 1,
        frequency_penalty: 0,
        presence_penalty: 0,
      });

    // Extract the generated response from the ChatGPT API
    // const chatGptResponse = response.data
    const chatResponse = response

    // Send the response back to the frontend
    res.send({ message: chatResponse});
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send({ error: 'An error occurred' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});