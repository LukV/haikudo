import os

async def write_response(response, filename):
    if not os.path.exists("responses"):
        os.makedirs("responses")
    with open(f"responses/{filename}.txt", "w") as f:
        f.write(response)
