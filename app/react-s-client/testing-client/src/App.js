import { useEffect, useState } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";

const App = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    console.log("WebSocket Client Connection...");
    const client = new W3CWebSocket("ws://localhost:8080");

    client.onopen = () => {
      console.log("WebSocket Client Connected");
    };

    client.onmessage = (message) => {
      setMessage(message.data);
    };

    return () => {
      client.close();
    };
  }, []);

  return (
    <div>
      <h1>Response from Server:</h1>
      <p>{message}</p>
    </div>
  );
};

export default App;
