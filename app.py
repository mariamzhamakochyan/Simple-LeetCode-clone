from flask import Flask, render_template, request

app = Flask(__name__)

problems = [
    {
        'id': 1,
        'title': 'Palindrome Number',
        'description': 'Given an integer x, return true if x is a palindrome, and false otherwise.',
        'difficulty': 'Easy',
    },
    {
        'id': 2,
        'title': 'Add Two Numbers',
        'description': 'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.',
        'difficulty': 'Medium',
    },
    {
        'id': 3,
        'title': ' Merge k Sorted Lists',
        'description': 'You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.Merge all the linked-lists into one sorted linked-list and return it.',
        'difficulty': 'Hard',
    },
]

@app.route('/')
def index():
    return render_template('index.html', problems=problems)

@app.route('/problem/<int:problem_id>', methods=['GET', 'POST'])
def problem(problem_id):
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if not problem:
        return 'Problem not found'

    if request.method == 'POST':
        solution = request.form['solution']
        return 'Solution submitted'

    return render_template('problem.html', problem=problem)



if __name__ == '__main__':
    app.run(debug=True)
