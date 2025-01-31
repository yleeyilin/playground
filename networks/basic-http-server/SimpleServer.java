import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * `curl http://localhost:8080`
 */
public class SimpleServer {
    public static void main(String[] args) throws IOException {
        int port = 8080; // binded port
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server running on port " + port);
            while (true) {
                Socket clientSocket = serverSocket.accept(); 
                handleClient(clientSocket); 
            }
        }
    }

    private static void handleClient(Socket socket) throws IOException {
        try (InputStream inputStream = socket.getInputStream();
             OutputStream outputStream = socket.getOutputStream()) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            String requestLine = reader.readLine(); // Reads GET / HTTP/1.1
            System.out.println("Request: " + requestLine);

            String response = "HTTP/1.1 200 OK\n" +
                   "Content-Type: text/plain\n" +
                   "Content-Length: 13\n"+
                   "\n" +
                   "Hello, World!\n";

            outputStream.write(response.getBytes()); 
        } finally {
            socket.close(); 
        }
    }
}
