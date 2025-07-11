async function submitPrompt() {
  const prompt = document.getElementById("prompt").value;
  const responseDiv = document.getElementById("response");

  if (!prompt) {
    responseDiv.textContent = "❌ Please enter a prompt.";
    return;
  }

  responseDiv.textContent = "⏳ Generating scene...";

  try {
    const res = await fetch("http://127.0.0.1:5000/api/prompt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt })
    });

    const data = await res.json();

    if (res.ok) {
      responseDiv.textContent = `✅ Success: ${data.message}`;
    } else {
      responseDiv.textContent = `❌ Error: ${data.error}`;
    }
  } catch (err) {
    responseDiv.textContent = `❌ Network error: ${err.message}`;
  }
}
