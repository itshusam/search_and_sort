from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(video_titles, target):
    left, right = 0, len(video_titles) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_title = video_titles[mid]

        if mid_title == target:
            return mid  
        elif mid_title < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"title": video_titles[index]}), 200
    else:
        return jsonify({"error": "Video not found"}), 404

app.run(debug=True)
