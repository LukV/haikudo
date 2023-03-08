from api import call_api
import click

@click.command()
@click.option("--topic", 
    prompt="Enter a topic", 
    help="The topic you want haikudo to proze out on.")
def run_api(topic):
    response = call_api(generate_prompt(topic))
    click.echo(response)

def generate_prompt(topic):
    return "Write a haiku about {}".format(topic)

def main():
    run_api()

if __name__ == '__main__':
    main()