import { useState } from "react";
import "./ChatWidget.css";export default function ChatWidget() {
const [open, setOpen] = useState(false);
const [msgs, setMsgs] = useState([
{
role: "bot",
text: "Hi! I'm your insurance assistant. Ask me anything about policies, claims, or coverage."
},
]);
const [text, setText] = useState("");
const [loading, setLoading] = useState(false);async function send() {
const msg = text.trim();
if (!msg || loading) return;// Add user message
setMsgs((m) => [...m, { role: "user", text: msg }]);
setText("");
setLoading(true);try {
  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg }),
  });  if (!res.ok) {
    throw new Error(`HTTP error! status: ${res.status}`);
  }  const data = await res.json();  // Add bot response
  setMsgs((m) => [...m, { role: "bot", text: data.answer }]);} catch (error) {
  console.error("Error:", error);
  setMsgs((m) => [
    ...m,
    { 
      role: "bot", 
      text: "Sorry, I'm having trouble connecting to the server. Please make sure the backend is running on port 8000." 
    },
  ]);
} finally {
  setLoading(false);
}
}function handleKeyPress(e) {
if (e.key === "Enter" && !e.shiftKey) {
e.preventDefault();
send();
}
}return (
<>
<button
className="chat-fab"
onClick={() => setOpen(!open)}
aria-label={open ? "Close chat" : "Open chat"}
>
{open ? "×" : "💬 Chat"}
</button>  {open && (
    <div className="chat-modal">
      <div className="chat-header">
        <span>Insurance Help</span>
        <button 
          className="close-btn" 
          onClick={() => setOpen(false)}
          aria-label="Close"
        >
          ×
        </button>
      </div>      <div className="chat-body">
        {msgs.map((m, i) => (
          <div key={i} className={`bubble ${m.role}`}>
            {m.text}
          </div>
        ))}
        {loading && (
          <div className="bubble bot loading">
            <span></span>
            <span></span>
            <span></span>
          </div>
        )}
      </div>      <div className="chat-input">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type your question..."
          onKeyDown={handleKeyPress}
          disabled={loading}
        />
        <button 
          onClick={send} 
          disabled={loading || !text.trim()}
        >
          {loading ? "..." : "Send"}
        </button>
      </div>
    </div>
  )}
</>
);
}