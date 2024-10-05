from flask import Flask, jsonify

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

def merge_sort(video_titles):
    if len(video_titles) <= 1:
        return video_titles

    mid = len(video_titles) // 2
    left_half = merge_sort(video_titles[:mid])
    right_half = merge_sort(video_titles[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list

@app.route('/sort', methods=['GET'])
def sort_videos():
    sorted_titles = merge_sort(video_titles)
    return jsonify({"sorted_videos": sorted_titles}), 200



app.run(debug=True)