# ElevenLabs WebSearch Webhook

This is a minimal Flask app that provides a `/websearch` POST endpoint compatible with ElevenLabs Conversational AI agents. It uses SerpAPI to return live search results.

## 🔧 Setup (Local or Render)

1. Clone this repo.
2. Install requirements:

```
pip install -r requirements.txt
```

3. Set your SerpAPI key:

```
export SERP_API_KEY=your_key_here
```

4. Run the app:

```
python app.py
```

## 🔥 Example POST Payload

```json
{
  "query": "latest UFO news"
}
```

## 🌐 Returns

```json
{
  "results": [
    {
      "title": "Article Title",
      "url": "https://example.com",
      "snippet": "Short preview"
    }
  ]
}
```

## 🧠 Purpose

Built for ElevenLabs agent integration to enable live web search capabilities via tools.

