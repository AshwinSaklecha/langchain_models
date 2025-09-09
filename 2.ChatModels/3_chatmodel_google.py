from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
result = model.invoke("Who is Magnus Carlsen")
print(result.content)

# Got this text - Magnus Carlsen is a Norwegian chess grandmaster.  He is widely regarded as the greatest chess player of all time, having held the world chess championship title since 2013.  Beyond his championship title, he's known for his aggressive playing style, exceptional intuition, and remarkable ability to calculate variations in chess.  He's also a popular figure in the chess world, known for his engaging personality and contributions to popularizing the game.
