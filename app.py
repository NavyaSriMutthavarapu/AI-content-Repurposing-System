from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['POST'])
def transcript():

    data = request.json
    print("Received Data:", data)

    video_id = data["videoId"]
    print("Video ID:", video_id)
    print("Type:", type(video_id))

    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id)

        text = " ".join([item.text for item in transcript_data])

        return jsonify({
            "transcript": text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)