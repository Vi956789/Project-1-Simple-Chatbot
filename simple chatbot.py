import random
from string import punctuation


def greet():
  """Greets the user with a friendly message."""
  greetings = ["Hi there!", "Hello! How can I help you today?", "Hey! What's on your mind?"]
  return random.choice(greetings)


def farewell():
  """Bids farewell to the user."""
  farewells = ["Bye! Have a great day!", "See you later!", "It was nice chatting with you! "]
  return random.choice(farewells)


def ask_question(question, context):
  """Asks the user a question and updates the context (if provided)"""
  user_input = input(question + " ")
  if context:
      context["user_answer"] = user_input.lower().translate(str.maketrans('', '', punctuation))
  return user_input


def answer_basic(question, context):
  """Provides pre-defined answers to common questions, considering context."""
  answers = {
      "what is your name?": "I don't have a specific name, but you can call me Chatty!",
      "how are you?": "I'm doing well, thanks for asking!",
      "what can you do?": "I can have simple conversations and learn as we interact!",
      "what's the weather like?": "Unfortunately, I can't access real-time weather information yet.",
      "what do you like to do?": "As a large language model, I don't have hobbies in the same way humans do. But I enjoy processing information and learning new things!",
  }
  return answers.get(question.lower(), "Hmm, I'm still learning about that. Can you rephrase?")


def remember(context, key, value):
  """Stores user responses in the context dictionary."""
  if context:
      context[key] = value


def recall(context, key):
  """Retrieves previously stored user responses."""
  if context:
      return context.get(key)


def main():
  """Maintains the conversation flow."""
  context = {}  # Initialize context dictionary

  print(greet())

  # Basic Q&A with additional questions
  for _ in range(7):
    question = ask_question("Ask me anything (or type 'bye' to exit): ", context)
    if question.lower() == "bye":
      break
    answer = answer_basic(question, context)
    print(answer)

  # User Interaction with Context

  name = ask_question("What's your name?", context)
  print(f"Nice to meet you, {name}!")
  remember(context, "name", name)

  remembered_name = recall(context, "name")
  if remembered_name:
    print(f"Welcome back, {remembered_name}! What would you like to talk about today?")
  else:
    location = ask_question("Where are you from?", context)
    print(f"Interesting! I've never chatted with someone from {location} before.")

  hobby = ask_question("What do you like to do for fun?", context)
  remember(context, "hobby", hobby)
  print(f"That sounds like fun! Maybe I can learn more about {hobby} sometime.")

  movie_genre = ask_question("What's your favorite movie genre?", context)
  remember(context, "genre", movie_genre)
  print(f"Interesting! I can recommend some movies in the {movie_genre} genre if you'd like.")

  print(farewell())


if __name__ == "__main__":
  main()
