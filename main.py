from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/age")
def get_age():
    try:
        date_of_birth = request.args.get("birthday")
        if not date_of_birth:
            raise Exception("Es necesaria una fecha de cumpleaños para calcular la edad")
        
        # Get the current date
        now = datetime.now()

        # Parse the user's input into a datetime object
        birthday = datetime.strptime(date_of_birth, "%Y-%m-%d")

        # Calculate the difference between the current date and the birthday
        difference = now - birthday

        # Calculate the person's age in years
        age_in_years = difference.days // 365
        
        # create output json
        response = {"age":age_in_years}
        
        return response
    
    except Exception as e:
        print(f"Algo salio mal: {str(e)}")


if __name__ == "__main__":
  app.run()