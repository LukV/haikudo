# haikudo
The `haikudo` package is the perfect tool for anyone who wants to express their love for their favorite subjects in the elegant and concise form of haiku poetry. 

But haikudo is not just about generating haikus. It also comes with a range of customization options that allow users to fine-tune their haikus to their liking. From adjusting the tone and mood of the haiku to choosing the specific words and phrases that will be used, haikudo puts the power of haiku creation in the hands of its users. 

So whether you're looking to impress your friends with your haiku skills or simply want to express your appreciation for your favorite subjects in a creative and unique way, haikudo is the perfect tool for you.

## Usage

### 1. Add an OpenAI API key

Clone this project and add an OpenAPI to it:
1. Sign up for an account with https://platform.openai.com/
2. Create an API under your account https://platform.openai.com/account/api-keys. Copy to key to your clipboard.
3. In the haikudo directory, create a copy of the file `.env.example` to `.env`.
4. Paste the API key in `.env`.

### 2. Install the necessary packages into your virtual environment

1. Create a virtual environment `python -m venv /path/to/new/virtual/environment`
2. Install the required packages `pip install -r requirements.txt`

### 2. Run haikudo from the command line

1. Run python cli.py --topic "Dead Parrot" --mood "Exasperated"
2. View the response on the command line
3. Find the result stored in the /responses directory




