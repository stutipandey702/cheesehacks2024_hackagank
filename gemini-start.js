import dotenv from "dotenv";
import readline from "readline";
import { GoogleGenerativeAI } from "@google/generative-ai";

dotenv.config();

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});


async function run() {
	const genAI = new GoogleGenerativeAI("AIzaSyDWrba1laxu5rJicJGZTajmpVhtJ--wCds");
	const model = genAI.getGenerativeModel({ model: "gemini-pro" });

	const chat = model.startChat({
		history: [], // start with empty history
		generationConfig: {
			maxOutputTokens: 500,
		}
	})

	async function askAndRespond() {
		rl.question("You: ", async (msg) => {
			if (msg.toLowerCase() === "exit") {
				rl.close
			} else {
				const result = await chat.sendMessage(msg);
				const response = await result.response;
				const text = await response.text();
				console.log("AI: ", text);
				askAndRespond();
			}
		})
	}

	askAndRespond();
}

run();